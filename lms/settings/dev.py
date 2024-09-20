import os # noqa
from lms.settings.components.base import * # noqa
from lms.settings.components.database_dev import * # noqa
from lms.settings.components.dev_tools import * # noqa
from lms.settings.components.celery import * # noqa
from lms.settings.components.rest_api import * # noqa
from lms.settings.components.email import * # noqa


DEBUG = True

ALLOWED_HOSTS = ['*']
