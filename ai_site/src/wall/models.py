from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from src.comment.models import AbstractComment


class Post(models.Model):
    """Post model
    """
    text = models.TextField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'id {self.id}'

    def comments_count(self):
        return self.comments.count()
    
    
class Comment(AbstractComment, MPTTModel):
    """comment model to posts
    """

    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,
        verbose_name="User",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        verbose_name="Post",
        related_name="comments",
        on_delete=models.CASCADE
    )

    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.user} - {self.post}"
