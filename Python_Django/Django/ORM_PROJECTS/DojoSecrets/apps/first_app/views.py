from django.shortcuts import render, redirect

from .models import User, Like, Secret

# Create your views here.

def index(request):
    if 'errors' not in request.session:
        request.session['errors'] = 0
    return render(request, "first_app/index.html")

def register(request):
    result = User.objects.register(request.POST, request)
    if result == True:
        request.session['logged_user_name'] = request.POST['email']
        return redirect('/secrets')
    else:
        return redirect('/')

def login(request):
    result = User.objects.login(request.POST, request)
    if result == True:
        request.session['logged_user_name'] = User.objects.only('first_name').get(email=request.POST['login_email']).first_name
        return redirect('/secrets')
    else:
        return redirect('/')

def secrets(request):
    context = {
        "users" : User.objects.all(),
        "secrets" : Secret.objects.all()
    }
    return render(request, 'first_app/secrets.html', context)

def popular_secrets(request):
    context = {
        "secrets" : Secret.objects.all(),
        "likes" : Like.objects.all()
    }
    return render(request, 'first_app/popular_secrets.html', context)

def post(request):
    Secret.objects.create(contet=request.POST['content'], user_id=request.session['id'])
    return reditect('/secrets')

def process_like(request, secret_id ):
     secret_id =int(Secret.objects.only('id').get(user_id=secret_id).id)
     Like.objecrts.create(user_id="", secret_id="")


    return redircet('/secrets')
