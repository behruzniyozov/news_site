import logging
import json
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from django.utils.timezone import make_aware
from celery.schedules import timedelta
from .models import News

logger = logging.getLogger(__name__)

@receiver(post_save, sender=News)
def create_publish_task(sender, instance, created, **kwargs):
    if instance.is_public and not instance.is_published:
        scheduled_time = instance.published_date + timedelta(hours=1)

        schedule, _ = ClockedSchedule.objects.get_or_create(
            clocked_time=make_aware(scheduled_time)
        )

        task_name = f'Publish News {instance.id}'

        PeriodicTask.objects.update_or_create(
            name=task_name,
            defaults={
                'clocked': schedule,
                'task': 'news.tasks.arrenged_publish_task',
                'args': json.dumps([instance.id]),
                'one_off': True,
                'enabled': True,
            }
        )
        logger.info(f"Scheduled publication for news: {instance.title}")
