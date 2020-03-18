from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Department, Level, Material, University, Faculty, Review, Subscriber
from blog.models import Post, Category
from accounts.models import Profile
from .forms import ReviewForm, MaterialSearchForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from urllib.parse import quote
# Create your views here.


def index(request):
    faculties = Faculty.objects.all()
    departments = Department.objects.all()
    levels = Level.objects.all()
    latest_posts = Post.objects.all()[:4]

    form = MaterialSearchForm(request.POST or None)

    context = {
        'faculties' : faculties,
        'departments' : departments,
        'levels' : levels,
        'latest_posts' : latest_posts,
        'form' : form
    }
    return render(request, 'main/index.html', context)

def load_depts(request):
    faculty = request.GET.get('faculty')
    departments = Department.objects.filter(faculty_id=faculty).order_by('name')

    context = {
        'departments' : departments
    }
    return render(request, 'main/dept_dropdown.html', context)

# @login_required
def material_search(request):
    level = Level.objects.get(id=request.POST.get('level'))
    faculty = Faculty.objects.get(id=request.POST.get('faculty'))
    department = Department.objects.get(id=request.POST.get('department'))


    materials = Material.objects.filter(level=level, faculty=faculty, department=department)

    paginator = Paginator(materials, 4)
    page = request.GET.get('page')

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)

    context = {
        'materials' : paginated_qs
    }
    return render(request, 'main/material_search_results.html', context)


def university_list(request):
    universities = University.objects.all()

    paginator = Paginator(universities, 4)
    page = request.GET.get('page')

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)

    context = {
        'universities' : paginated_qs
    }

    return render(request, 'main/universities.html', context)

def university_detail(request, slug):
    university = University.objects.get(slug=slug)
    materials = Material.objects.filter(university=university)

    paginator = Paginator(materials, 4)
    page = request.GET.get('page')

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)
    
    context = {
        'university' : university,
        'materials' : paginated_qs
    }
    return render(request, 'main/university_detail.html', context)


def course_list(request, slug):
    department = Department.objects.get(slug=slug)
    materials = Material.objects.filter(department=department)

    context = {
        'department' : department,
        'materials' : materials
    }
    return render(request, 'main/course_list.html', context)
    


def course_detail(request, slug):
    course = Material.objects.get(slug=slug)
    reviews = Review.objects.filter(material=course)
    related_courses = Material.objects.filter(department=course.department, university=course.university).exclude(id=course.id)[:4]
    departments = Department.objects.all()
    share_string = quote(course.desc)
    url_string = quote(str(request.build_absolute_uri()))

    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            review = request.POST.get('review')
            form.instance.user = request.user
            form.instance.material = course
            form.save()

            return redirect('main:course', slug=course.slug)

    context = {
        'course' : course,
        'reviews' : reviews,
        'form' : form,
        'related_courses' : related_courses,
        'departments' : departments,
        'share_string' : share_string,
        'url_string' : url_string
    }
    return render(request, 'main/course-detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent.')
            return redirect('/')
    else:
        form = ContactForm(request.POST or None)
    context = {
        'form':form
    }
    return render(request, 'main/contact.html', context)


def search(request):
    _queryset = Post.objects.all()
    query = request.GET.get('q')
    categories = Category.objects.all()

    if query:
        queryset = _queryset.filter(
            Q(title__icontains=query) |
            Q(desc__icontains=query)
        ).distinct()
    
    paginator = Paginator(queryset, 4)
    page = request.GET.get('page')

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)
    
    context = {
        'queryset' : paginated_qs,
        'query' : query,
        'categories' : categories
    }

    return render(request, 'main/search.html', context)

def course_search(request):
    _queryset = Material.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = _queryset.filter(
            Q(name__icontains=query) |
            Q(desc__icontains=query)
        ).distinct()
    
    paginator = Paginator(queryset, 4)
    page = request.GET.get('page')

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)
    
    
    context = {
        'materials' : paginated_qs,
        'query' : query
    }

    return render(request, 'main/course_search.html', context)


def about(request):
    len_posts = len(Post.objects.all())
    len_users = len(Profile.objects.all())
    len_materials = len(Material.objects.all())
    len_universities = len(University.objects.all())

    context = {
        'no_of_posts' : len_posts,
        'no_of_users' : len_users,
        'no_of_materials' : len_materials,
        'no_of_universities' : len_universities
    }
    return render(request, 'main/about.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_subscriber = Subscriber.objects.create(email=email)
        new_subscriber.save()
        messages.success(request, 'You have suscribed successfully.')
        return redirect('main:index')

def handler_404(request):
    pass

def handler_500(request):
    pass

