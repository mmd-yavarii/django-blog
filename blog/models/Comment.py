from django.db import models
from django.contrib.auth.models import User
from .Post import Post

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    content = models.TextField(null=False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f"{self.post.title} comment"

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=('-created_at',))
        ]
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"