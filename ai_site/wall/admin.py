from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from wall.models import Comment, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """post"""
    
    list_display = ("user", "published", "create_date", "moderation", "view_count", "id")
    

@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """comments to post"""

    list_display = ("user", "post", "create_date", "updated_date", "published", "id")
    #actions = ['unpublish', 'publish']
    mptt_level_indent = 15
    
# Register your models here.
