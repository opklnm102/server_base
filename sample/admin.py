from django.contrib import admin

from sample.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    change_form_template = "sample/admin/change_form.html"

    list_display = ['id', 'user', 'name', 'url', 'created']
    date_hierarchy = 'created'
    raw_id_fields = ['user', ]
