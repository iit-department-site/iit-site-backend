

from django.db.models.query import QuerySet

from rest_framework import generics, permissions, viewsets, response
from rest_framework.serializers import Serializer
from wall.serializers import ListPostSerializer
from base.classes import MixedPermission

from .services import feed_service



class FeedView( viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPostSerializer
    
    def list(self, request, *args, **kwargs):
        
        queryset = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many = True)
        return response.Response(serializer.data)
        