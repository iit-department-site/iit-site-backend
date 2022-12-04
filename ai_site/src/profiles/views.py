from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import ListAPIView
from .models import UserNet, Technology
from rest_framework.decorators import action
from .serializers import (
    GetUserNetSerializer,
    GetUserNetPublicSerializer,
    UserAvatarSerializer,
    TechnologySerializer,
    TechnologyImageSerializer
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class UserNetList(ListAPIView):
    queryset = UserNet.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = GetUserNetPublicSerializer
    permissions = (permissions.AllowAny,)


class UserNetPublicView(ModelViewSet):
    """
    CRUD methods for UserNetPublic Model
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = (permissions.AllowAny,)


class UserNetView(ModelViewSet):
    """
    CRUD methods for UserNet model
    """
    serializer_class = GetUserNetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)


class UserAvatarView(GenericViewSet):
    queryset = UserNet.objects.all()
    serializer_class = UserAvatarSerializer

    @action(detail=False, methods=["get"])
    def get_avatar(self, request, pk):
        instance = self.queryset.get(pk=pk)
        serialized_data = self.serializer_class(instance)
        return Response(serialized_data.data)

    @action(detail=False, methods=["put", "post"])
    def upload_avatar(self, request, pk):
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception:
            return Response("user not found", status=status.HTTP_404_NOT_FOUND)


class TechnologyViewSet(ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TechnologyImageViewSet(ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologyImageSerializer

    @action(detail=False, methods=["get"])
    def get_tech_image(self, request, pk):
        instance = self.queryset.get(pk=pk)
        serialized_data = self.serializer_class(instance)
        return Response(serialized_data.data)

    @action(detail=False, methods=["put", "post"])
    def upload_tech_image(self, request, pk):
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception:
            return Response("tech not found", status=status.HTTP_404_NOT_FOUND)
