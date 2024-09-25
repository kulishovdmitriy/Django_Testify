from django.apps import AppConfig


class GroupsConfig(AppConfig):
    """

    Configures the groups app for the Django project.

    Attributes:
        default_auto_field (str): Specifies the type of primary key to use by default for models in the app.
        name (str): The name of the app, used to reference it within the Django project.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groups'
