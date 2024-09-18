#!/bin/bash

rm -f /tmp/celerybeat-schedule /tmp/celerybeat.pid

celery -A lms beat -l info --schedule=/tmp/celerybeat-schedule --pidfile=/tmp/celerybeat.pid