from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def process(request):
    username = User.objects.login(request.POST['username'])
    if username == True:
        User.objects.create(username = request.POST['username'])
        return redirect ('/success')
    else:
        request.session['error'] = username['error']
        return redirect('/')

def success(request):
    context = {
        "users" : User.objects.all()
    }
    #below we will get the most recent username and assign it to session
    latest = len(context['users']) - 1
    context['current'] = context['users'][latest]


    request.session.clear()
    return render(request, 'first_app/success.html', context)
