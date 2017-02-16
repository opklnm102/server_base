from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django_summernote.admin import SummernoteModelAdmin
from .tasks import dump_board_post_task
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'name', 'slug']
    list_filter = ['parent']
    list_editable = ['parent', 'name', 'slug']


def post_dump_view(request):
    dump_board_post_task.delay()
    messages.success(request, 'board_post 데이터 덤프 작업을 시작하였습니다.')
    return redirect(request.META.get('HTTP_REFERER', '/'))


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    change_form_template = 'board/admin/post_change_form.html'
    change_list_template = 'board/admin/post_change_list.html'
    list_display = ['id', 'categories_display', 'title', 'user', 'tags_display', 'created', 'modified', 'view_link']
    date_hierarchy = 'created'
    raw_id_fields = ['user', ]

    def categories_display(self, obj):
        return ','.join([i.name for i in obj.categories.all()])

    categories_display.short_description = '분류'

    def tags_display(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    tags_display.short_description = '태그'

    def view_link(self, obj):
        return "<a href='{}'>보기</a>".format(reverse('admin:post-view', kwargs={'pk': obj.id}))

    view_link.short_description = '보기'
    view_link.allow_tags = True

    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        my_urls = [
            url(r'^(?P<pk>\d+)/view/$', self.post_view, name="post-view"),
            url(r'^dump/$', post_dump_view, name="post-dump"),
        ]
        return my_urls + urls

    def post_view(self, request, pk):
        context = dict(
            self.admin_site.each_context(request),
            object=get_object_or_404(Post, id=pk),
            opts=self.model._meta,
        )
        return render(request, "board/admin/post_view.html", context)
