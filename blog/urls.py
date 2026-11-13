from django.urls import path
from .view import post_list , post_details , ticket, add_post, profile, signup_view, login_view, logout_view, change_info_view, reset_password_view

app_name = "blog"

urlpatterns = [
    path(route='' , view=post_list , name="posts_list"), 
    path(route="posts/<uuid:id>/" , view=post_details , name="post_details"),
    path(route="ticket/" , view=ticket , name="ticket"),
    path(route="add-post/" , view=add_post, name="add_post"), 
    path(route="profile/" , view=profile , name="profile"), 
    path(route="signup/" , view=signup_view, name="signup"), 
    path(route="login/" , view=login_view, name="login"), 
    path(route="logout/" , view=logout_view, name="logout"), 
    path(route='change-info/' , view=change_info_view , name="change_info"), 
    path(route="reset-password/" , view=reset_password_view, name="reset_password")
]