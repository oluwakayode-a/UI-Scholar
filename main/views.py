from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Department, Level, Material, University, Faculty, Review
from blog.models import Post
from .forms import ReviewForm, MaterialSearchForm
from django.contrib.auth.decorators import login_required
import datetime
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

    context = {
        'materials' : materials
    }
    return render(request, 'main/material_search_results.html', context)


def university_list(request):
    universities = University.objects.all()

    context = {
        'universities' : universities
    }

    return render(request, 'main/universities.html', context)

def university_detail(request, slug):
    university = University.objects.get(slug=slug)
    departments = Department.objects.filter(university=university)
    materials = Material.objects.filter(university=university)
    
    context = {
        'university' : university,
        'materials' : materials
    }
    return render(request, 'main/university_detail.html', context)


def course_list(request):
    pass

def course_detail(request, slug):
    course = Material.objects.get(slug=slug)
    reviews = Review.objects.filter(material=course)
    related_courses = Material.objects.filter(department=course.department, university=course.university)[:4]

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
        'related_courses' : related_courses
    }
    return render(request, 'main/course-detail.html', context)


def contact(request):
    context = {}
    return render(request, 'main/contact.html', context)

def search(request):
    q = request.GET.get('query')
    pass

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def handler_404(request):
    pass

def handler_500(request):
    pass

