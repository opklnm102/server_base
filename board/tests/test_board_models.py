from test_plus.test import TestCase
from model_mommy.mommy import make as mm

from board.models import Category, Post


class TestCategoryModel(TestCase):
    def test_create_category(self):
        news = mm(Category, name='뉴스', slug='news')
        news.save()
        breaking = mm(Category, parent=news, name='속보', slug='breaking')
        assert news.is_root
        assert not breaking.is_root
        assert Category.root_objects.all().count() == 1
        assert Category.objects.all().count() == 2


class TestPostModel(TestCase):
    def test_create_post(self):
        category_news = mm(Category, name='뉴스', slug='news')
        category_technology = mm(Category, parent=category_news, name='기술', slug='technology')
        post = mm(Post, title='내용입니다.')
        post.categories.add(category_technology)
        assert post.__str__() == '내용입니다.'
        assert post.categories.all().count() == 1
        assert category_technology.post_set.all().count() == 1
        assert Post.objects.filter(categories__parent=category_news).count() == 1
