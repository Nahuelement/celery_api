from datetime import timedelta

from dcelery.celery_config import app

import logging

logger = logging.getLogger(__name__)


app.conf.beat_schedule = {
    # 'task1':{
    #     'task': 'dcelery.celery_tasks.ex12_task_schedule_customization.task1',
    #     'schedule': timedelta(seconds=20),
    #     'kwargs': {'foo': 'bar'},
    #     'args': (1.5, 5),
    #     'options': {
    #         'queue':'tasks',
    #         'priory':5,
    #     }
    # },
    'task2':{
        'task': 'newapp.tasks.management_command',
        'schedule': timedelta(seconds=10),
    }
}

@app.task(queue="tasks")
def task1(a, b, **kwargs):
    result = a*b
    logger.info(f"Running task 1 - {result}")

@app.task(queue="tasks")
def task2():
    logger.info("Running task 2")