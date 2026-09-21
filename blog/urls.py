from django.urls import path
from .view import *

app_name = "blog"

urlpatterns = [
    path(route='' , view=post_list , name="posts_list"), 
    path(route="posts/<uuid:id>" , view=post_details , name="post_details")
]