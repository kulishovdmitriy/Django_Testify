from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserAction(models.Model):
    """
    Represents an action performed by a user, such as login, logout, or profile changes.

    Enum USER_ACTION:
        Provides a set of predefined actions that a user can perform.
        LOGIN: User logged in
        LOGOUT: User logged out
        CHANGE_PASSWORD: User changed password
        CHANGE_PROFILE: User changed profile
        CHANGE_PROFILE_IMAGE: User changed profile image

    Attributes:
        user: A ForeignKey to the User model, representing the user who performed the action.
        write_date: A DateTimeField that records the date and time when the action was logged.
        action: A PositiveSmallIntegerField that stores the type of action performed, chosen from USER_ACTION choices.
        info: An optional CharField that can store additional information about the action, with a maximum length of 128 characters.
    """

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
    """
    A Django model that represents a user's profile which extends the built-in User model.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model. Deletes profile when user is deleted.
        image (ImageField): An optional field to upload a profile picture. Defaults to 'pictures/default.jpg'.
        interests (CharField): An optional field to store user interests, with a maximum length of 128 characters.
        email_opened (BooleanField): A boolean field indicating whether the user has opened an email. Defaults to False.
    """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(null=True, default='pictures/default.jpg', upload_to='pictures/')
    interests = models.CharField(max_length=128, null=True)
    email_opened = models.BooleanField(default=False)


class BlockedUser(models.Model):
    """
    Represents a blocked user in the system.

    Attributes:
        user (OneToOneField): A one-to-one relationship to the User model.
        blocked_at (DateTimeField): The date and time when the user was blocked. Automatically set to the current date and time when the entry is created.
        reason (CharField): The reason why the user was blocked, can be null.

    Methods:
        __str__(): Returns a string representation of the blocked user.
    """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    blocked_at = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user.username} is blocked! Reason: {self.reason}, blocked_at: {self.blocked_at}"
