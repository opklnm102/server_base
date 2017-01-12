from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from board.permissions import IsOwnerAndAdminOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerAndAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
