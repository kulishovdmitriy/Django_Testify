from django.apps import AppConfig


class StudentsConfig(AppConfig):
    """

    Class representing the configuration for the 'students' Django application.

    Attributes:
        default_auto_field (str): Specifies the default type of primary key field to use for models.
        name (str): The name of the application being configured.

    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
