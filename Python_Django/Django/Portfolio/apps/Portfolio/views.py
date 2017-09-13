from django.shortcuts import render

def index(request):
     return render(request, "Portfolio/index.html")
     
def testimonials(request):
    return render(request, "Portfolio/testimonials.html")
