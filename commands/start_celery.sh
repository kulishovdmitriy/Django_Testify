#!/bin/bash

echo "Waiting for RabbitMQ to be ready..."

sleep 5

celery -A lms worker -l info -c "$CELERY_NUM_WORKERS"