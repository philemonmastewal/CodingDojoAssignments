#CONTROLLER!!!!
from django.shortcuts import render, HttpResponse
#the index function is called when root is visited
def index(request):
    print ("*"*75)
    return render(request, "first_app/index.html")
def show(request):
    print (request.method) #to show what method is hitting this route
    return render(request, "first_app/showusers.html")




    # response = "Hello, I am your first request!"
    # return HttpResponse(response)

# Create your views here.
