from django.apps import AppConfig


class TeachersConfig(AppConfig):
    """
    Configuration class for the 'teachers' application.

    This class inherits from Django's AppConfig and is used to configure settings
    specific to the 'teachers' application. The default primary key field type is set
    to 'BigAutoField', and the name of the application is specified as 'teachers'.

    Attributes:
    default_auto_field: Specifies the type of primary key to use for models.
    name: The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teachers'
