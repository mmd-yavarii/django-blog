
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Post (models.Model):
    id = models.UUIDField(primary_key=True , editable=False , default=uuid4 , verbose_name="شناسه")
    title = models.CharField(max_length=100 , verbose_name="عنوان" , help_text="عنوان باید حداکثر ۱۰۰ کاراکتر باشد")
    description = models.TextField(null=True , blank=True , verbose_name="توضیحات")
    slug = models.SlugField(unique=True , verbose_name="اسلاگ")
    is_deleted = models.BooleanField(default=False)

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

    def __str__ (self):
        return self.title

    class Meta:
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["-created_at"])
        ]

        verbose_name = "پست"
        verbose_name_plural = "پست ها"