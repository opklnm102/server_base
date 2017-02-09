from django.db import models


class StandAlone(models.Model):
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
