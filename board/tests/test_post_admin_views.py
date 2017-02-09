from model_mommy.mommy import make as mm

from board.tests.test_post_views import mommy_make_user
from danbi.testcases import TestCaseWithoutRouter as TestCase
from ..models import Post


class TestPostAdminViewCase(TestCase):
    def test_post_view(self):
        staff = mommy_make_user(is_staff=True)
        post = mm(Post)
        with self.login(staff):
            self.get_check_200('admin:post-view', pk=post.id)
