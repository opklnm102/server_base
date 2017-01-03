from test_plus.test import TestCase


class TestHomeViews(TestCase):
    def test_home_view(self):
        self.get('home')
        self.assertInContext('test')
        self.response_200()

    def test_error_view(self):
        self.get('error404')
        self.response_404()
        res = self.get('error500')
        assert res.status_code == 500
