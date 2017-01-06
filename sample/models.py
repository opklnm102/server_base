import jsonfield
from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Bookmark(TimeStampedModel):
    name = models.CharField('이름', max_length=100)
    url = models.URLField('주소')
    user = models.ForeignKey(User, null=True)
    data = jsonfield.JSONField()
