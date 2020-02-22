from django.shortcuts import render, redirect
from .forms import ProjectSubmissionForm

# Create your views here.
def index(request):
    return render(request, 'project_mgt/index.html', {})

def submit(request):
    form = ProjectSubmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'project_mgt/submit.html', context)