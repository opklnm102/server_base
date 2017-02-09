from django.contrib.auth.models import User
from test_plus.test import TestCase

from board.models import Post
from model_mommy.mommy import make as mm


class TestReadSlaveOnlyRouter(TestCase):
    def test_write(self):
        post = mm(Post)
        assert post._state.db == 'default'

    def test_read(self):
        user = User.objects.db_manager('slave').create_user(username='test')
        Post.objects.db_manager('slave').create(title='test', content='test', user=user)
        post = Post.objects.first()
        assert post._state.db == 'slave'
