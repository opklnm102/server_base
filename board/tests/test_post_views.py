import json

from django.contrib.auth.models import User
from model_mommy.mommy import make as mm
from test_plus.test import TestCase

from ..models import Post, Category


def mommy_make_user(**kwargs):
    user = mm(User, **kwargs)
    user.set_password('password')
    user.save()
    return user


class TestPostViewCase(TestCase):
    def setUp(self):
        self.user = mommy_make_user()
        self.user_other = mommy_make_user()
        self.user_staff = mommy_make_user(is_staff=True)
        self.category_news = mm(Category, name='뉴스', slug='news')
        self.category_technology = mm(Category, parent=self.category_news, name='기술', slug='technology')
        self.posts = mm(Post, user=self.user, _quantity=3)
        for post in self.posts:
            post.categories.add(self.category_technology)

    def test_list_view(self):
        response = self.get_check_200('board:post-list')
        assert response.json()['results'].__len__() == 3
        post = self.posts[0]
        self.get_check_200('board:post-detail', pk=post.id)

        with self.login(username=self.user):
            self.post(
                'board:post-list',
                data={'title': 'hi', 'content': 'a',
                      'categories': [self.category_news.id, self.category_technology.id]}
            )
            self.response_201()
            self.put(
                'board:post-detail', pk=post.id,
                data=json.dumps({'title': 'hi', 'content': 'b',
                                 'categories': [self.category_technology.id, ]}),
                extra={'content_type': 'application/json'}
            )
            self.response_200()

        with self.login(username=self.user_other):
            self.get_check_200('board:post-list')
            self.put(
                'board:post-detail', pk=post.id,
                data={'title': 'hi', 'content': 'c', }
            )
            self.response_403()

        with self.login(username=self.user_staff):
            self.post(
                'board:post-list',
                data={'title': 'notice', 'content': "I'm staff",
                      'categories': [self.category_news.id, self.category_technology.id]}
            )
            self.response_201()
            response = self.put(
                'board:post-detail', pk=post.id,
                data=json.dumps({'title': 'hi', 'content': 'edited by staff',
                                 'categories': [self.category_news.id, ]}),
                extra={'content_type': 'application/json'}
            )
            assert post.user.id == response.json().get('user')
            self.response_200()
