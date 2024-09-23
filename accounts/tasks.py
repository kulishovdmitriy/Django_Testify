from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True, max_retries=3)
def send_activation_email_task(self, subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@shared_task
def send_contact_email(subject, message, from_email):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[settings.EMAIL_HOST_RECIPIENT],
        fail_silently=False,
    )
