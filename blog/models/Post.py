
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from jdatetime import datetime
from django.utils import timezone

from uuid import uuid4


class ModelManager (models.Manager):
    def get_archived (self):
        return self.filter(is_deleted=True)

class PublishedManager (models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post (models.Model):
    id = models.UUIDField(primary_key=True , editable=False , default=uuid4 , verbose_name="شناسه")
    title = models.CharField(max_length=100 , verbose_name="عنوان" , help_text="عنوان باید حداکثر ۱۰۰ کاراکتر باشد")
    description = models.TextField(null=True , blank=True , verbose_name="توضیحات")
    slug = models.SlugField(unique=True , verbose_name="اسلاگ")
    is_deleted = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    image = models.ImageField(upload_to="posts/",null=True,blank=True,verbose_name="تصویر")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Status (models.TextChoices):
        DRAFT = ("DR" , "در انتظار تایید")
        PUBLISHED = ("PB" , "منتشر شده")
        REJECTED = ("RJ", "رد شده")

    status = models.CharField(choices=Status.choices , default=Status.DRAFT, verbose_name="وضعیت")

    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="posts", verbose_name="نویسنده")
    likes = models.ManyToManyField(User, related_name="likes", blank=True , verbose_name="لایک ها")
    comments = models.ManyToManyField(User , related_name="comments" , blank=True , through="Comment" , verbose_name="کامنت ها")

    objects = ModelManager()
    published = PublishedManager()

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse("blog:post_details" , kwargs={"id" : self.id})

    @property
    def likes_count (self):
        return self.likes.count()

    @property
    def comments_count (self):
        return self.comments.count()

    @property
    def persian_created_date (self):
        formatted = datetime.fromgregorian(datetime=self.created_at).strftime("%Y/%m/%d - %H:%M")
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

    def delete(self, *args , **kwargs):
        self.is_deleted = True
        self.save()

    class Meta:
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["-created_at"])
        ]

        verbose_name = "پست"
        verbose_name_plural = "پست ها"