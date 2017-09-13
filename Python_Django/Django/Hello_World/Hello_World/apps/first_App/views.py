from django.shortcuts import render


def index(request):
    print "*"*75
    return render(request, "first_App/index.html")
