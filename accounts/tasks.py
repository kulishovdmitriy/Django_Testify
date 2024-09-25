from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True, max_retries=3)
def send_activation_email_task(self, subject, message, from_email, recipient_list):
    """
    Celery task to send an activation email.

    This task is responsible for sending an activation email by
    using Django's `send_mail` function. If an exception occurs
    during the sending process, the task retries up to 3 times
    with a countdown of 60 seconds between retries.

    Parameters:
    self : task instance
    subject : str
        Subject of the email to be sent.
    message : str
        Body of the email to be sent.
    from_email : str
        Email address from which the email is sent.
    recipient_list : list
        List of recipient email addresses.
    """

    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@shared_task
def send_contact_email(subject, message, from_email):
    """
    Celery shared task for sending a contact email.

    This task uses Django's send_mail function to send an email with the given subject, message,
    and from_email address to the recipient defined in the EMAIL_HOST_RECIPIENT setting.

    Parameters:
    - subject: The subject of the email.
    - message: The body content of the email.
    - from_email: The sender's email address.
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[settings.EMAIL_HOST_RECIPIENT],
        fail_silently=False,
    )
