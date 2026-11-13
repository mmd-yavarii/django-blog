from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_http_methods , require_GET , require_POST
from ..forms import SignupForm, LoginForm , ChangeUserInfoForm
from django.contrib.auth import login , authenticate , logout
from ..models import Post

import secrets
from django.core.mail import send_mail
from django.conf import settings

# send email function 
def send_code(user_email, subject="کد احراز هویت"):

    code = secrets.randbelow(900000) + 100000

    message = f"کد احراز هویت شما: {code}"

    html_message = f"""
    <div dir="rtl" style="font-family: Tahoma; text-align: center;">
        <h2>کد احراز هویت</h2>
        <h1 style="color: #2563eb;">{code}</h1>
        <p>این کد تا ۵ دقیقه معتبر است.</p>
    </div>
    """

    result = send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        html_message=html_message,
        fail_silently=False,
    )

    return code if result == 1 else None

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


# logout 
@login_required
@require_POST
def logout_view (request):
    logout(request)
    return redirect("blog:login")



# profile 
@login_required
def profile (request):
    user = request.user 
    posts = Post.objects.filter(author=user)
    return render(request , "auth/profile.html", {"user" : user, "posts" : posts})


# change user info 
@login_required
@require_http_methods(["POST" , "GET"])
def change_info_view (request):
    if request.method == "POST":
        form = ChangeUserInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("blog:profile")
    else:
        form = ChangeUserInfoForm(instance=request.user)
    return render(request, "auth/change-info.html" , {"form" : form})



# reset password 
@require_http_methods(["GET" , "POST"])
def reset_password_view (request):
    code = send_code("mdyavarii@gmail.com")
    print(code)
    render(request, "auth/reset-password.html" , {"form" : {}})