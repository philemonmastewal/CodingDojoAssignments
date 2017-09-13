from django.shortcuts import render, redirect

from . models import User

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    result = User.objects.register(request.POST, request)
    if result == True:
        request.session['logged_user'] = request.POST['email']
        return redirect('/success')
    else:
        return redirect('/')

def login(request):
    result = User.objects.login(request.POST, request)
    if result == True:
        request.session['logged_user'] = request.POST['login_email']
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, 'first_app/success.html', context)
