import os # noqa
from lms.settings.components.base import * # noqa
from lms.settings.components.database_staging_prod import * # noqa
from lms.settings.components.celery_prod import * # noqa
from lms.settings.components.rest_api import * # noqa
from lms.settings.components.email import * # noqa


DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(':')

STATIC_ROOT = '/var/www/web_universe/static'

MEDIA_ROOT = '/var/www/web_universe/media'
