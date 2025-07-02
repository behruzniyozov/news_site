import logging
import json
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from django.utils import timezone
from celery.schedules import timedelta
from .models import News

logger = logging.getLogger(__name__)

@receiver(post_save, sender=News)
def create_publish_task(sender, instance, created, **kwargs):
    if instance.is_public and not instance.is_published:
        # Schedule time: 2 minutes from now
        scheduled_time = timezone.now() + timedelta(minutes=1)

        # No need to call make_aware here, scheduled_time is already timezone-aware
        schedule, _ = ClockedSchedule.objects.get_or_create(
            clocked_time=scheduled_time
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

        logger.info(f"Scheduled publication for news: {instance.title} at {scheduled_time}")
