from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import ListAPIView
from .models import UserNet
from rest_framework.decorators import action
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer, UserAvatarSerializer
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

    # def post(self, request, format=None):
    #     serializer = PhotoSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, format=None):
    #     photo = self.get_object(pk)
    #     serializer = PhotoSerializer(photo, data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["put"])
    def upload_avatar(self, request, pk):
        instances = self.queryset.filter(pk=pk)

        instances.update(avatar=request.FILES.get("avatar"))
        # print(request)
        # print('ADADSASD')
        # #serialized_data = self.serializer_class(data=request.data)
        # print(serialized_data)
        return Response(status=status.HTTP_200_OK)

