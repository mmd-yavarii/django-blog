
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):

    error_messages = {
        "password_mismatch": "رمزهای عبور با یکدیگر مطابقت ندارند.",
    }

    email = forms.EmailField(
        required=True,
        label="ایمیل",
        error_messages={
            "required": "وارد کردن ایمیل الزامی است.",
            "invalid": "فرمت ایمیل معتبر نیست.",
        }
    )

    password1 = forms.CharField(
        label="کلمه عبور",
        widget=forms.PasswordInput,
        help_text="""
            رمز عبور شما باید:
            حداقل ۸ کاراکتر داشته باشد،
            خیلی ساده یا قابل حدس نباشد،
            صرفاً شامل اعداد نباشد،
            و بیش از حد شبیه اطلاعات شخصی شما نباشد.
        """,
        error_messages={
            "required": "وارد کردن رمز عبور الزامی است.",
        }
    )

    password2 = forms.CharField(
        label="تکرار کلمه عبور",
        widget=forms.PasswordInput,
        error_messages={
            "required": "تکرار رمز عبور الزامی است.",
        }
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

        labels = {
            "username": "نام کاربری",
        }

        help_texts = {
            "username": "حداکثر ۱۵۰ کاراکتر؛ فقط حروف، اعداد و کاراکترهای @ . + - _ مجاز هستند.",
        }

        error_messages = {
            "username": {
                "required": "وارد کردن نام کاربری الزامی است.",
                "max_length": "نام کاربری حداکثر باید ۱۵۰ کاراکتر باشد.",
                "invalid": "نام کاربری شامل کاراکترهای غیرمجاز است.",
            }
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "این ایمیل قبلاً در سامانه ثبت شده است."
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user
