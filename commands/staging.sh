#!/bin/bash

gunicorn -w ${WORKERS} -b "0:${PORT}" lms.wsgi:application --log-level=${LOG_LEVEL}