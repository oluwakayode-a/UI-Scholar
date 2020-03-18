from blog.models import Post

def recent_posts(request):
    recent_posts = Post.objects.all()[:2]

    return {
        'recent_posts' : recent_posts
    }