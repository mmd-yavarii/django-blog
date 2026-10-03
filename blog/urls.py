from django.urls import path
from .view import post_list , post_details

app_name = "blog"

urlpatterns = [
    path(route='' , view=post_list , name="posts_list"), 
    path(route="posts/<uuid:id>/" , view=post_details , name="post_details")
]