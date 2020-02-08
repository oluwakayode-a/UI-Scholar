from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Level, Material, University, Faculty
import datetime
# Create your views here.


def index(request):
    faculties = Faculty.objects.all()
    departments = Department.objects.all()
    levels = Level.objects.all()

    context = {
        'faculties' : faculties,
        'departments' : departments,
        'levels' : levels
    }
    return render(request, 'main/index.html', context)

def material_search(request):
    level = Level.objects.get(name=request.POST.get('level'))
    faculty = Faculty.objects.get(name=request.POST.get('faculty'))
    department = Department.objects.get(name=request.POST.get('department'))


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
    
    context = {
        'university' : university
    }
    return render(request, 'main/university.html', context)


def course_list(request):
    pass

def course_detail(request):
    pass


def contact(request):
    context = {}
    return render(request, 'main/contact.html', context)

def search(request):
    pass

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def handler_404(request):
    pass

def handler_500(request):
    pass

