#!/bin/bash

echo "launch in PROD mode..."

gunicorn -w ${WORKERS} -b "0:${PORT}" lms.wsgi:application --log-level=${LOG_LEVEL}