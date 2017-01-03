from test_plus.test import TestCase


class TestHomeViews(TestCase):
    def test_home_view(self):
        self.get('home')
        self.assertInContext('test')
        self.response_200()
