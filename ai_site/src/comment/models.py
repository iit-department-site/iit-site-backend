from django.db import models

# Create your models here.
class AbstractComment(models.Model):
    text = models.TextField("Message", max_length=512)
    create_date = models.DateTimeField("Created at", auto_now_add=True)
    updated_date = models.DateTimeField("Updated at", auto_now_add=True)
    published = models.BooleanField("Publish?", default=True)
    deleted = models.BooleanField("Deleted?", default=False)
    
    
    def __str__(self):
        return f"{self.text}"
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        abstract = True