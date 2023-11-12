#!/bin/bash
source /env/source/activate

celery -A ai_assistant.celery worker  --loglevel=info

