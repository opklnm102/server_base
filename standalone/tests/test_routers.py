from django.db.utils import ProgrammingError
from django.test import TestCase

from standalone.models import StandAlone


class TestStandAloneRouter(TestCase):
    multi_db = True

    def test_write(self):
        try:
            standalone = StandAlone.objects.create(title='title', content='content')
            assert standalone._state.db == 'standalone'
            print('hit')
        except ProgrammingError:
            pass

    def test_read(self):
        try:
            StandAlone.objects.create(title='title', content='content')
            standalone = StandAlone.objects.first()
            assert standalone._state.db == 'standalone'
            print('hit')
        except ProgrammingError:
            pass
