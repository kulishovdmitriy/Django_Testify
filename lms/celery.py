import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"lms.settings.{os.environ.get('RUN_MODE', 'dev')}")

app = Celery('lms')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
