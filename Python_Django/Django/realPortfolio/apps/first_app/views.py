from django.shortcuts import render, redirect

def index(request):
    return render (request, "first_app/index.html")

def projects(request):
    return render (request, "first_app/projects.html")
def about(request):
    return render (request, "first_app/about.html")
def testimonials(request):
    return render (request, "first_app/testimonials.html")
def create(request):
    if request.method == "POST":
        print "*"*75
        print request.POST
        print request.method
        print "*"*75
        request.session['name']=request.POST['first_name']
        return redirect("/")
    else:
        return redirect("/")

# Create your views here.
