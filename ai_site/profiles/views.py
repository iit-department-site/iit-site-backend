from rest_framework.generics import RetrieveAPIView
from .models import UserNet
from .serializers import GetUserNetSerializer 


class GetUserNetView(RetrieveAPIView):
    '''out profile info'''
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer