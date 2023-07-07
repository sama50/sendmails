import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendmails.settings')

app = Celery('sendmails')
 
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

 
app.conf.beat_schedule = {
    'generate_weekly_triggers': {
        'task': 'app.tasks.send_scheduled_mails',
        'schedule': 1,
    }
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')