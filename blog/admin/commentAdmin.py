from django.contrib import admin
from ..models import Comment
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):

    list_display = ["id",'user_name','post_list','persian_created_date']

    @admin.display(description="User")
    def user_name(self, obj):
        url = reverse("admin:auth_user_change",args=[obj.user.id])
        return format_html("<a href='{}'>{}</a>",url,obj.user.username)

    @admin.display(description="Post")
    def post_list(self, obj):
        url = reverse("admin:blog_post_change",args=[obj.post.id])
        return format_html("<a href='{}'>{}</a>",url,obj.post.title)