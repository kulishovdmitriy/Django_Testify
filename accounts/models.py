from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserAction(models.Model):
    class USER_ACTION(models.IntegerChoices):
        LOGIN = 0, "Login"
        LOGOUT = 1, "Logout"
        CHANGE_PASSWORD = 2, "Change Password"
        CHANGE_PROFILE = 3, "Change Profile"
        CHANGE_PROFILE_IMAGE = 4, "Change Profile image"

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    write_date = models.DateTimeField(auto_now_add=True)
    action = models.PositiveSmallIntegerField(choices=USER_ACTION.choices)
    info = models.CharField(max_length=128, null=True)


class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(null=True, default='pictures/default.jpg', upload_to='pictures/')
    interests = models.CharField(max_length=128, null=True)
