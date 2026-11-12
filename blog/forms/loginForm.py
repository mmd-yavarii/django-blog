
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        required=True,
        label="نام کاربری",
        error_messages={
            "required": "وارد کردن نام کاربری الزامی است."
        }
    )

    password = forms.CharField(
        required=True,
        label="کلمه عبور",
        widget=forms.PasswordInput,
        error_messages={
            "required": "وارد کردن کلمه عبور الزامی است."
        }
    )

    error_messages = {
        "invalid_login": "نام کاربری یا کلمه عبور اشتباه است.",
        "inactive": "حساب کاربری شما غیرفعال است."
    }
