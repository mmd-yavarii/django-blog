from django.http import JsonResponse
from ..models import Post, Comment


def post_details(request, id):

    if request.method != "GET":
        return JsonResponse({"message" : "bad request"} , status=400)

    post = Post.published.get(id=id)
    comments = Comment.objects.filter(post=post)

    context = {
        "post": {
            "id": str(post.id),
            "title": post.title,
            "description": post.description,
            "author": post.author.username,
            "likes_count": post.likes_count,
            "comments_count": post.comments_count
        },

        "comments": list(
            comments.values(
                "id",
                "content",
                "created_at",
                "user__username"
            )
        ),
    }

    return JsonResponse(
        {"message": "message", "data": context},
        status=200
    )