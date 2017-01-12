from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'name', 'slug']
    list_filter = ['parent']
    list_editable = ['parent', 'name', 'slug']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    def categories_display(self, obj):
        return ','.join([i.name for i in obj.categories.all()])

    categories_display.short_description = '분류'

    def tags_display(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    tags_display.short_description = '태그'
    list_display = ['id', 'categories_display', 'title', 'user', 'tags_display', 'created', 'modified']
    date_hierarchy = 'created'
    raw_id_fields = ['user', ]
