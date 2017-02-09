from test_plus.test import TestCase

from standalone.models import StandAlone
from model_mommy.mommy import make as mm


class TestStandAloneRouter(TestCase):
    def test_write(self):
        standalone = mm(StandAlone)
        assert standalone._state.db == 'standalone'

    def test_read(self):
        StandAlone.objects.db_manager('standalone').create(title='test', content='test content')
        standalone = StandAlone.objects.first()
        assert standalone._state.db == 'standalone'
