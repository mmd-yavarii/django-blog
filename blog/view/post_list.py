from django.http import JsonResponse
from ..models import Post
from django.db.models import Q


def post_list(request):

    search_value = request.GET.get("search")
    user_filter = request.GET.get("author")

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

    context = {
        "data": list(data.values())
    }

    return JsonResponse(
        {"message": "message", "data": context},
        status=200
    )