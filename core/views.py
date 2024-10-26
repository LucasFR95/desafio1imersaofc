from django.shortcuts import get_object_or_404, render
from core.models import Post

def blog_index(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "core/blog.html", context)

def blog_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'core/blog_post.html', {'post': post})