from django.contrib import admin , messages
from ..models import Post

from django.urls import reverse
from django.utils.html import format_html
from jdatetime import datetime



@admin.action(description="آرشیو کردن")
def archive (modeladmin , request , queryset):
    if request.user.username == "mmd_yavarii":
        queryset.update(is_deleted=True)
        modeladmin.message_user(request , "با موفقیت آرشیو شد", messages.SUCCESS)
    else :
        modeladmin.message_user(request , "امکان آرشیو کردن برای این کاربر وجود ندارد", messages.ERROR)



@admin.action(description="حذف از آرشیو")
def unarchive (modeladmin , request , queryset):
    if request.user.username == "mmd_yavarii":
        queryset.update(is_deleted=False)
        modeladmin.message_user(request , "با موفقیت از آرشیو حذف شد", messages.SUCCESS)
    else :
        modeladmin.message_user(request , "امکان حذف از آرشیو برای این کاربر وجود ندارد", messages.ERROR)



@admin.register(Post)
class Post_Admin (admin.ModelAdmin):
    list_display = ["is_deleted", "title" , "author_link", "status", "custom_created_at"]
    list_display_links = ["title"]
    list_editable = ["status"]  
    list_filter = ["is_deleted" , "status" , "author__username"]
    search_fields = ["author__username" , "title" , "description" , "slug"]
    date_hierarchy = "created_at"
    list_per_page = 10 
    ordering = ["-created_at"]
    readonly_fields = ["id"]
    raw_id_fields = ["author" , "comments" , "likes"]
    actions = [archive, unarchive]

    @admin.display(description="نویسنده")
    def author_link (self , obj):
        url = reverse("admin:auth_user_change", args=[obj.author.id])
        return format_html("<a href='{}'>{}</a>", url , obj.author.username)

    @admin.display(description="تاریخ")
    def custom_created_at (self , obj):
        formatted = datetime.fromgregorian(datetime=obj.created_at).strftime("%Y/%m/%d - %H:%M")
        return formatted