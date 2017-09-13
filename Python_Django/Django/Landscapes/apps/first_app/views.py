from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def landscapes(request, landscape_number):
    context = {
        "landscape_number" : int(landscape_number)
    }

    return render(request, 'first_app/landscapes.html', context)
