# from celery.schedules import crontab


CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq_dev:5672//'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# CELERY_BEAT_SCHEDULE = {
#
#     'some_task': {
#         'task': 'core.tasks.run_email_info',  # TODO tasks (path core/tasks create func 'run_email_info')
#         'schedule': crontab(minute='*/2'),
#     },
#
#     'run_server_task': {
#         'task': 'core.tasks.run_server_info',  # TODO tasks (path core/tasks create func 'run_server_info')
#         'schedule': crontab(minute='*/2'),
#     }
# }
