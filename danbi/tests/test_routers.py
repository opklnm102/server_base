from django.contrib.auth.models import User
from django.test import TestCase

from board.models import Post


class TestReadSlaveOnlyRouter(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test-master')
        self.post = Post.objects.create(title='title', user=user, content='content')

    def test_write(self):
        assert self.post._state.db == 'default'

    def test_read(self):
        user = User.objects.db_manager('slave').create_user(username='test')
        Post.objects.db_manager('slave').create(title='test', content='test', user=user)
        post = Post.objects.first()
        assert post._state.db == 'slave'
