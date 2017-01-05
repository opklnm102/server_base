from django.contrib.auth.models import User
from model_mommy.mommy import make as mm
from test_plus.test import TestCase

from ..models import Bookmark


class TestBookmarkModelCase(TestCase):
    def test_bookmark_create_view(self):
        user = mm(User)
        bookmark = mm(Bookmark, user=user, name='test', url='https://test.com')
        assert bookmark.name == 'test'
        assert Bookmark.objects.filter(name='test').count() == 1
