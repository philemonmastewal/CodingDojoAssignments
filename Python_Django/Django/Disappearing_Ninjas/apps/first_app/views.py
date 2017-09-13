from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def allNinjas(request):
    context = {
        "allNinjas" : True
    }

    return render(request, 'first_app/ninjas.html', context)

def ninjasColor(request, ninja_color):
    context = {
        "allNinjas" : False,
        "ninja_color" : ninja_color
    }
    print (ninja_color)

    return render(request, 'first_app/ninjas.html', context)
