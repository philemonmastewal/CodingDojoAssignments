from django.shortcuts import render, HttpResponse
import random #<-- with this you can use random.shuffle to shuffle the VALUES list before serving the desired amount of items from it

VALUES = ["This is string 1","This is string 2","This is string 3","This is string 4","This is string 5","This is string 6","This is string 7","This is string 8","This is string 9","This is string 10",] #<-- this list will be populated with strings

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def show(request):
    random.shuffle(VALUES)
    numberPicked = request.POST['numberPicked']
    output = []
    for count in range(0, int(numberPicked)):
        output.append(VALUES[count])
        
    context = {
        "values" : output,
        "numberPicked" : numberPicked
    }

    return render(request, 'first_app/show.html', context)
