from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """
    Список постов.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        AuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Комментарии к посту.
    """
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        instance_post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=instance_post)


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet
                    ):
    """Список подписок."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('following__username',)
    ordering_fields = ('following',)

    def perform_create(self, serializer: FollowSerializer):
        """Создает подписку. Подписчик - текущий юзер."""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Возвращает список подписок."""
        return self.request.user.follower.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Группы."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
