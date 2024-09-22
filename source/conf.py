# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from dotenv import load_dotenv


sys.path.insert(0, os.path.abspath('..'))

load_dotenv()

os.environ['DJANGO_SETTINGS_MODULE'] = 'lms.settings.staging'

import django # noqa

django.setup()


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'University'
copyright = '2024, Dmitriy'
author = 'Dmitriy'
release = 'v.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]


SECRET_KEY = os.environ.get('SECRET_KEY')
PORT = os.environ.get('PORT')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
WORKERS = os.environ.get('WORKERS')
CELERY_NUM_WORKERS = os.environ.get('CELERY_NUM_WORKERS')
EMAIL_HOST_RECIPIENT = os.environ.get('EMAIL_HOST_RECIPIENT')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

viewcode_follow_imports = 'import'
