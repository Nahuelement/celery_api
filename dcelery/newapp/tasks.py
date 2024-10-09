import time

from celery import group, shared_task
from django.core.management import call_command
from dcelery.celery_config import app
import logging

logger = logging.getLogger(__name__)


@app.task(queue="tasks")
def management_command():
    print("Probando tasks folder")

# @shared_task
# def tp1(queue='celery'):
#     time.sleep(3)
#     return

# @shared_task
# def tp2(queue='celery:1'):
#     time.sleep(3)
#     return

# @shared_task
# def tp3(queue='celery:2'):
#     time.sleep(3)
#     return

# @shared_task
# def tp4(queue='celery:3'):
#     time.sleep(3)
#     return