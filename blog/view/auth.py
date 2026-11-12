from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_http_methods , require_GET , require_POST
from ..forms import SignupForm, LoginForm
from django.contrib.auth import login , authenticate , logout
from ..models import Post


# create account 
@require_http_methods(["GET" , "POST"])
def signup_view (request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("blog:profile")
    else:
        form = SignupForm()

    return render(request, "auth/signup.html", {"form" : form})


# login 
@require_http_methods(["GET" , "POST"])
def login_view (request):
    if request.method == "POST":
        form = LoginForm(request , request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect("blog:profile")
    else :
        form = LoginForm(request)
    return render(request , "auth/login.html", {"form": form})


# profile 
@login_required
def profile (request):
    user = request.user 
    posts = Post.objects.filter(author=user)
    return render(request , "auth/profile.html", {"user" : user, "posts" : posts})



# logout 
@login_required
@require_POST
def logout_view (request):
    logout(request)
    return redirect("blog:login")