from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy.mommy import make as mm

from board.models import Post
from standalone.models import StandAlone


class TestStandAloneRouter(TestCase):
    def setUp(self):
        self.standalone = mm(StandAlone)

    def test_write(self):
        assert self.standalone._state.db == 'standalone'
        post = mm(Post)
        assert post._state.db == 'default'

    def test_read(self):
        standalone = StandAlone.objects.first()
        assert standalone._state.db == 'standalone'
        user = User.objects.db_manager('slave').create_user(username='test_alone')
        Post.objects.db_manager('slave').create(title='test', content='test', user=user)
        post = Post.objects.first()
        assert post._state.db == 'slave'
