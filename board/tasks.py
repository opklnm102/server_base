from __future__ import absolute_import

import logging

from board.management.commands.dump_board_post import dump_post
from danbi.celery import app

logger = logging.getLogger(__name__)


@app.task
def dump_board_post_task():
    rows = dump_post()
    logger.info('{} posts'.format(rows))
