from django.core.management.base import BaseCommand
from django.db import connection

TABLE_NAME = {
    'origin': 'board_post',
    'copy': 'board_post_copy'
}

SQL = {
    'exists_copy': "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='{}');".format(
        TABLE_NAME['copy']),
    'create_copy': "CREATE TABLE {} AS TABLE {};".format(
        TABLE_NAME['copy'], TABLE_NAME['origin']),
    'truncate': "TRUNCATE TABLE {} CONTINUE IDENTITY RESTRICT;".format(
        TABLE_NAME['copy']),
    'copy': "INSERT INTO {} SELECT * FROM {};".format(
        TABLE_NAME['copy'], TABLE_NAME['origin']),
}


def table_exists(cursor):
    cursor.execute(SQL['exists_copy'])
    return cursor.fetchone()[0]


def dump_post(debug=False):
    def p(message):
        if debug:
            print(message)

    cursor = connection.cursor()
    if table_exists(cursor):
        p('board_post_copy table 이미 있음')
    else:
        cursor.execute(SQL['create_copy'])
        p('board_post_copy table 생성')
    cursor.execute(SQL['truncate'])
    p('board_post_copy table 비우기')
    cursor.execute(SQL['copy'])
    p('board_post 에서 값 가져오기')
    cursor.close()


class Command(BaseCommand):
    help = '게시판 Post 전체를 별도의 테이블에 덤프하기'

    def handle(self, *args, **options):
        dump_post(True)
