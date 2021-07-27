from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


class UserNetPublicView(ModelViewSet):
    """out public user profile """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]
    
    
class UserNetView(ModelViewSet):
    """ out profile user"""
    
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
    
    