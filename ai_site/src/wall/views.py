from rest_framework import permissions, generics

from base.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from base.permissions import IsAuthor, IsMemberGroup, IsAuthorEntry, IsAuthorCommentEntry
from .models import Post, Comment
from .serializers import CreateCommentSerializers, PostSerilizer, ListPostSerializer


class PostListView(generics.ListAPIView):
    """Post list of user"""

    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk')).select_related('user').prefetch_related('comments')


class PostView(CreateRetrieveUpdateDestroy):
    """CRUD post"""
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerilizer

    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def preform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class CommentsView(CreateUpdateDestroy):
    """Put comments to post"""
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializers

    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def preform_destroy(self, instance):
        instance.deleted = True
        instance.save()  # скрываем, но не удаляем
