from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
    "time": datetime.now(),
    }
    return render(request, 'first_app/index.html', context)
# Create your views here.
