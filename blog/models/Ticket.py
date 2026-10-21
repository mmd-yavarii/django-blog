from django.db import models
from django.core.validators import RegexValidator

phone_regex = r"^09\d{9}$"
phone_regex_message = "شماره موبایل باید با 09 شروع شود و 11 رقم باشد."

class Ticket(models.Model):
    message = models.TextField(verbose_name="پیام")
    name = models.CharField(max_length=200, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=11, verbose_name="شماره تلفن" , validators=[RegexValidator(regex=phone_regex , message=phone_regex_message)])
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت‌ها"
        indexes = [
            models.Index(fields=["-created_at"]),
        ]