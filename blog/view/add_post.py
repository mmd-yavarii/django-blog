from django.shortcuts import render , redirect
from ..forms import PostForm

from django.contrib.auth.models import User
from ..models.Post import Post

def add_post (request):
    if request.method == "POST":
        form_obj = PostForm(request.POST, request.FILES)

        if form_obj.is_valid():
            cleaned = form_obj.cleaned_data
            user = User.objects.first()

            new_post = Post(
                title=cleaned["title"], 
                description=cleaned["description"],
                slug=cleaned["slug"],
                image=cleaned["image"],
                author=user,
            )
            new_post.save()

        context = {
            "form" : form_obj
        }

        return redirect("blog:posts_list")    
    else :
        form_obj = PostForm()
        context = {
            "form" : form_obj
        }
        return render(request, "forms/add_post.html", context)
