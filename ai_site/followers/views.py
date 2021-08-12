from followers.models import Follower
from profiles.models import UserNet
from followers.serializers import ListFollowerSerializer
from django.shortcuts import render
from rest_framework  import generics, permissions, views, response
# Create your views here.
class ListFollowerView(generics.ListView):
    """output list of subscribers"""
    
    
    permissions_classes = [permissions.IsAuthenticated]
    
    serializer_class = ListFollowerSerializer
    
    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)
    
    
class AddFollowerView(views.APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    
    def post(self, request, pk):
        
        user = UserNet.objects.filter(id=pk)
        if user.exists():
            """проверка на подписку"""
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        return response.Response(status=404)
       
 