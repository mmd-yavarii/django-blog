
from django.db import models
from django.contrib.auth.models import User
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

    image = models.ImageField(upload_to="media/posts/", null=True , blank=True, verbose_name="تصویر")

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

    @property
    def likes_count (self):
        return self.likes.count()

    @property
    def comments_count (self):
        return self.comments.count()

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