from django.shortcuts import render, get_object_or_404
from django.db.models import F
from ..models import Post, Comment


def post_details(request, id):

    post = get_object_or_404(
        Post.published,
        id=id
    )

    Post.published.filter(id=id).update(
        views=F("views") + 1
    )

    post.refresh_from_db()


    comments = Comment.objects.filter(
        post=post
    ).select_related(
        "user"
    ).order_by(
        "-created_at"
    )


    context = {
        "post": post,
        "comments": comments
    }


    return render(
        request,
        "post-details.html",
        context
    )