from rest_framework import serializers
from base.serializers import RecursiveSerializer, FilterCommentListSerializer
from .models import Post, Comment

class CreateCommentSerializers(serializers.ModelSerializer):
    """ add comment to post"""
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")
        


class ListCommentSerializer(serializers.ModelSerializer):
    """List of comments """
    
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')
    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text
    
    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id","user", "post", "text", "create_date", "updated_date", "deleted", "children" )
        

class PostSerilizer(serializers.ModelSerializer):
    """ GET and PUT post """
    
    user = serializers.ReadOnlyField(source='user.username')
    comments = ListCommentSerializer(many=True, read_only=True)
    view_count = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ("id","create_date", "user", "text", "comments", "view_count" )
        
        
class ListPostSerializer(serializers.ModelSerializer):
    """ list of posts"""
    
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments_count")        