from rest_framework import serializers

from sample.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'name', 'user', 'url', 'created', 'modified')
        read_only_fields = ('id', 'created', 'modified')
