from celery import shared_task

from .models import News


@shared_task
def arrenged_publish_task(news_id):
    """
    Task to arrange the publication of news.
    """
    try:
        news = News.objects.get(id=news_id)
        if not news.is_published:
            news.is_published = True
            news.save()
            print(f"News '{news.title}' has been published.")
        else:
            print(f"News '{news.title}' is already published.")
    except News.DoesNotExist:
        print(f"News with id {news_id} does not exist.")