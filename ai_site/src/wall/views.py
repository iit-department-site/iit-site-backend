from rest_framework import permissions, generics

from base.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from base.permissions import IsAuthor, IsMemberGroup, IsAuthorEntry, IsAuthorCommentEntry
from .models import Post, Comment
from .serializers import CreateCommentSerializers, PostSerilizer, ListPostSerializer
from rest_framework.pagination import PageNumberPagination


class PostListView(generics.ListAPIView):
    """
    endpoint which return list of Post model
    """

    serializer_class = ListPostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk')).select_related('user').prefetch_related('comments')


class PostView(CreateRetrieveUpdateDestroy):
    """
    CRUD methods for Post model
    """
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
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
    """
    Create, Update, Delete methods for Comment model
    """
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CreateCommentSerializers

    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def preform_destroy(self, instance):
        instance.deleted = True
        instance.save()  # скрываем, но не удаляем
