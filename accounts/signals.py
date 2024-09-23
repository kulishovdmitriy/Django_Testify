from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site

from accounts.models import Profile
from accounts.tasks import send_activation_email_task


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        request = kwargs.get('request')
        current_site = get_current_site(request) if request else None
        mail_subject = 'Activate your account'
        message = render_to_string('activation_email.html', {
            'user': instance,
            'domain': current_site.domain if current_site else 'example.com',
            'uidb64': urlsafe_base64_encode(force_bytes(instance.pk)),
            'token': token_generator.make_token(instance),
        })
        recipient_list = [instance.email]
        send_activation_email_task.delay(mail_subject, message, 'your_email@gmail.com', recipient_list)
