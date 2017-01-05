import json

from django.contrib.auth.models import User
from django.urls import reverse
from model_mommy.mommy import make as mm
from test_plus.test import TestCase

from ..models import Bookmark


class TestBookmarkViewCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = mm(User)
        cls.user.set_password('password')
        cls.user.save()
        cls.user_staff = mm(User, is_staff=True)
        cls.user_staff.set_password('password')
        cls.user_staff.save()

    def test_list_view(self):
        self.make_user('user1')
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
            response = self.client.put(
                reverse('sample:bookmark:bookmark-detail', args=[bookmark1.id]),
                data=json.dumps({'name': 'google', 'url': 'http://www.google.com', }),
                content_type='application/json'
            )
            assert response.status_code == 200
            assert Bookmark.objects.get(id=bookmark1.id).name == 'google'
