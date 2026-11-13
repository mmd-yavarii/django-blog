
from django.contrib.auth.models import User
from django import forms


class ChangeUserInfoForm(forms.ModelForm):

    email = forms.EmailField(
        label="ایمیل",
        error_messages={
            "required": "وارد کردن ایمیل اجباری است",
            "invalid": "فرمت ایمیل معتبر نیست"
        }
    )

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]

        labels = {
            "username": "نام کاربری",
            "first_name": "نام",
            "last_name": "نام خانوادگی"
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exclude(
            pk=self.instance.pk
        ).exists():
            raise forms.ValidationError(
                "این ایمیل قبلاً در سامانه ثبت شده است."
            )

        return email
