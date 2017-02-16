from __future__ import absolute_import
from danbi.celery import app

from board.management.commands.dump_board_post import dump_post


@app.task
def dump_board_post_task():
    dump_post()
