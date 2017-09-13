from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context= {
        "courses" : Course.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def process(request):
    Course.objects.create(name=request.POST['Name'], description=request.POST['Description'])
    print "course.name"
    return redirect('/')

def remove(request, id):
    context = {
        "id" : int(id),
        "course" : Course.objects.get(id=id)
    }
    return render(request, 'first_app/remove.html', context)
def destroy(request, id):
    context = {
        "id" : int(id)
    }
    Course.objects.filter(id=id).delete()
    return redirect( '/', context)
