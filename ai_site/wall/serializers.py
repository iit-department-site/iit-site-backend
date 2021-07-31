from rest_framework import serializers

from .models import Post, Comment

class CreateCommentSerializers(serializers.ModelSerializer):
    """ add comment to post"""
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")
        


class ListCommentEntryGroupSerializers(serializers.ModelSerializer):
    """List of comments """
    
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    
    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text
    
    class Meta:
        list_serializer_class = CreateCommentSerializers
        model = Comment
        fields = ("id", "post", "text", "create_date", "update_date", "deleted", "children" )
        

class PostSerilizer(serializers.ModelSerializer):
    """ GET and PUT post """
    
    user = serializers.ReadOnlyField(source='user.username')
    comment = ListCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ("id","create_date", "user", "text", "comment", "view_count" )
        
        
class ListPostSerializer(serializers.ModelSerializer):
    """ list of posts"""
    
    author = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        fields = ("id", "create_date", "author", "text", "comments_count")        