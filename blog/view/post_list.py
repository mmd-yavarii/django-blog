from ..models import Post
from django.db.models import Q
from django.shortcuts import render

from django.core.paginator import Paginator

def post_list(request):

    search_value = request.GET.get("search")
    user_filter = request.GET.get("author")
    page = request.GET.get("page" , 1)

    data = Post.published.all()

    if search_value:
        search_query = (
            Q(author__username__icontains=search_value)
            | Q(title__icontains=search_value)
            | Q(description__icontains=search_value)
        )
        data = data.filter(search_query)

    if user_filter:
        data = data.filter(author__username=user_filter)

    paginator = Paginator(data , 10) 

    context = {
        "posts": paginator.page(page), 
    }

    return render(request=request , template_name="post-list.html" , context=context)