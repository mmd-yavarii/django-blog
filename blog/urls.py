from django.urls import path
from .view import post_list , post_details , ticket, add_post

app_name = "blog"

urlpatterns = [
    path(route='' , view=post_list , name="posts_list"), 
    path(route="posts/<uuid:id>/" , view=post_details , name="post_details"),
    path(route="ticket/" , view=ticket , name="ticket"),
    path(route="add-post/" , view=add_post, name="add_post")
]