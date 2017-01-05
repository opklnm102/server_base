from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser

from sample.models import Bookmark
from sample.serializers import BookmarkSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = LimitOffsetPagination
