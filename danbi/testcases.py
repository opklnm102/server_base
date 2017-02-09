from django.test import override_settings
from test_plus import TestCase


@override_settings(DATABASE_ROUTERS=[])
class TestCaseWithoutRouter(TestCase):
    pass
