from django import forms
from django.core.validators import RegexValidator

phone_regex = r"^09\d{9}$"
phone_regex_message = "شماره موبایل باید با 09 شروع شود و 11 رقم باشد."

class ticketForm(forms.Form):
    SUBJECT_CHOICES = [
        ("suggestion", "پیشنهاد"),
        ("criticism", "انتقاد"),
        ("bug_report", "گزارش مشکل"),
    ]

    message = forms.CharField(widget=forms.Textarea,required=True,label="متن پیام", )
    name = forms.CharField(max_length=200,required=True,label="نام و نام خانوادگی",)
    email = forms.EmailField(required=True,label="آدرس ایمیل",)
    phone = forms.CharField(required=True,label="شماره موبایل", validators=[
        RegexValidator(regex=phone_regex , message=phone_regex_message)
    ])
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES,label="موضوع تیکت")