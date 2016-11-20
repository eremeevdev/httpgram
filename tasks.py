from celery import Celery

import requests
import db

from bot import bot

app = Celery('tasks', broker='redis://redis:6379/0')

app.conf.beat_schedule = {
    'check': {
        'task': 'tasks.check',
        'schedule': 30.0,
    },
}

app.conf.timezone = 'UTC'


@app.task
def check_url(url):

    status_code = requests.get(url).status_code
    history_log = db.get_last_status_log(url)

    if history_log is None or history_log['status_code'] != status_code:

        db.log_status(url, status_code)

        chat_list = db.get_chats_for_url(url)

        if status_code == 200:
            msg = 'UP: {}'.format(url)

        else:
            msg = 'DOWN: {}'.format(url)

        for chat in chat_list:
            bot.chat(chat).send(msg, preview=False)


@app.task
def check():
    for url in db.get_all_urls():
        check_url.delay(url)
