from django.contrib import admin

from sample.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'url', 'created']
    date_hierarchy = 'created'
    raw_id_fields = ['user', ]
