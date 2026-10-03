from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from jdatetime import datetime
from .Post import Post

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_comments")
    content = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.post.title} comment"

    @property
    def persian_created_date(self):
        formatted = datetime.fromgregorian(
            datetime=self.created_at
        ).strftime("%Y/%m/%d - %H:%M")
        return formatted

    @property
    def time_since_created(self):
        now = timezone.now()
        diff = now - self.created_at
        seconds = diff.total_seconds()
        if seconds < 60:
            return "همین الان"
        minutes = seconds // 60
        if minutes < 60:
            return f"{int(minutes)} دقیقه پیش"
        hours = minutes // 60
        if hours < 24:
            return f"{int(hours)} ساعت پیش"
        days = hours // 24
        if days < 30:
            return f"{int(days)} روز پیش"
        months = days // 30
        if months < 12:
            return f"{int(months)} ماه پیش"
        years = months // 12
        return f"{int(years)} سال پیش"



    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"])
        ]
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"