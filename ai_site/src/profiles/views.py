from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


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
    