import json

from django.contrib.auth.models import User
from model_mommy.mommy import make as mm

from danbi.testcases import TestCaseWithoutRouter as TestCase
from ..models import Bookmark


class TestBookmarkViewCase(TestCase):
    def setUp(self):
        self.user = mm(User)
        self.user.set_password('password')
        self.user.save()
        self.user_staff = mm(User, is_staff=True)
        self.user_staff.set_password('password')
        self.user_staff.save()

    def test_list_view(self):
        bookmark1 = mm(Bookmark, user=self.user)
        self.get('sample:bookmark:bookmark-list')
        self.response_403()
        with self.login(username=self.user.username):
            self.get('sample:bookmark:bookmark-list')
            self.response_403()
        with self.login(username=self.user_staff.username):
            self.get_check_200('sample:bookmark:bookmark-list')
            self.get_check_200('sample:bookmark:bookmark-detail', pk=bookmark1.id)
            response = self.post(
                'sample:bookmark:bookmark-list',
                data={'name': 'google', 'url': 'http://www.google.com', 'user': self.user.id}
            )
            bookmark_id = response.json().get('id')
            self.response_201()
            self.get_check_200('sample:bookmark:bookmark-detail', pk=bookmark_id)
            response = self.delete('sample:bookmark:bookmark-detail', pk=bookmark_id)
            self.assertEqual(response.status_code, 204)
            assert bookmark1.name != 'google'
            self.put(
                'sample:bookmark:bookmark-detail', pk=bookmark1.id,
                data=json.dumps({'name': 'google', 'url': 'http://www.google.com', }),
                extra={'content_type': 'application/json'}
            )
            self.response_200()
            assert Bookmark.objects.get(id=bookmark1.id).name == 'google'
