from django.shortcuts import render
from .models import Post, Category

# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    context = {
        'posts' : posts,
        'categories' : categories
    }

    return render(request, 'blog/index.html', context)


def category(request):
    q = request.GET.get('category')
    q = q.lower() # convert to slug version
    category = Category.objects.get(slug=q)
    categories = Category.objects.all()

    posts_in_category = Post.objects.filter(category=category)

    context = {
        'category' : category,
        'posts' : posts_in_category,
        'categories' : categories
    }

    return render(request, 'blog/category.html', context)
    