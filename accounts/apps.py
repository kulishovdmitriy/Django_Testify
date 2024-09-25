from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Class for configuring the 'accounts' application in a Django project.
    Manages app-specific settings and behavior.

    Attributes:
        default_auto_field: Specifies the type of auto-incrementing primary key field to be used.
        name: The name of the application.

    Methods:
        ready:
            Imports the signal configuration for the accounts application.
            Ensures that application-specific signals are loaded and connected at the correct time.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals # noqa
