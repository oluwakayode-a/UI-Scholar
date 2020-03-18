from django.shortcuts import render, redirect
from .models import Post, Category, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)

    context = {
        'posts' : paginated_qs,
        'categories' : categories
    }

    return render(request, 'blog/index.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()

    posts_in_category = Post.objects.filter(category=category)

    paginator = Paginator(posts_in_category, 4)
    page = request.GET.get('page')

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)

    context = {
        'category' : category,
        'posts' : paginated_qs,
        'categories' : categories
    }

    return render(request, 'blog/category.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    categories = Category.objects.all()
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id).order_by('time_stamp')[:2]

    form = CommentForm(request.POST or None)
    if form.is_valid():
        body = request.POST.get('body')
        form.instance.user = request.user
        form.instance.post = post
        form.save()

        return redirect(post.get_absolute_url())


    context = {
        'post' : post,
        'related_posts' : related_posts,
        'form' : form,
        'categories' : categories,
        'comments' : comments
    }

    return render(request, 'blog/post.html', context)
 