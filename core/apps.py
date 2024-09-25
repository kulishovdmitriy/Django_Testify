from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
     Represents the configuration for the 'core' application.
     Inherits from the Django AppConfig class.
     Defines the default_auto_field and application name.
     Attributes:
         default_auto_field: Specifies the default auto field to use for primary keys in models.
         name: The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
