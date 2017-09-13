from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):

    if 'count' in request.session:
        pass
    else:
        request.session['count'] = 0
    print (request.session['count'])
    return render(request,"first_app/index.html")
# Create your views here.
def new_word(request):
    if request.method == 'POST':
        request.session['randword'] = get_random_string(length=14)
        request.session['count'] += 1
        return redirect ('/')
    else:
        return redirect('/')
