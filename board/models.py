from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel
from taggit.managers import TaggableManager


class RootCategoryManager(models.Manager):
    def get_queryset(self):
        queryset = super(RootCategoryManager, self).get_queryset()
        return queryset.filter(parent__isnull=True)


class Category(models.Model):
    class Meta:
        verbose_name_plural = _('Categoires')

    name = models.CharField('이름', max_length=50)
    slug = models.SlugField('URL slug', max_length=50, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    objects = models.Manager()
    root_objects = RootCategoryManager()

    @property
    def is_root(self):
        return not bool(self.parent)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField('제목', max_length=200)
    user = models.ForeignKey(User, verbose_name='작성자')
    content = models.TextField('내용')

    categories = models.ManyToManyField(Category, verbose_name='분류', blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
