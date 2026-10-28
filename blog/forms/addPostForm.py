from django import forms
from ..models.Post import Post

class PostForm (forms.Form):
    title = forms.CharField(required=True , max_length=100 , label="عنوان")
    description = forms.CharField(widget=forms.Textarea, required=False, label="توضیحات")
    slug = forms.CharField(required=True , label="اسلاگ")
    image = forms.ImageField(required=False,label="تصویر")

    def clean_slug(self):
        slug = self.cleaned_data["slug"]

        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError(
                "این اسلاگ قبلاً استفاده شده است."
            )

        return slug