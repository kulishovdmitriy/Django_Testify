#!/bin/bash

python manage.py runserver "0:${PORT}" --settings="lms.settings.${RUN_MODE}"