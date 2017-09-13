from django.shortcuts import render, redirect

def index(request):
    if "count" in request.session:
        pass
    else:
        request.session['count'] = 0
    return render(request, "first_app/index.html")
def result(request):
    if request.method == 'POST':
        request.session['name']=request.POST["your_name"]
        request.session['dojolocation']=request.POST["dojo_location"]
        request.session['favoritelanguage']=request.POST["favorite_location"]
        request.session['comment']=request.POST["comment"]

        request.session['count'] += 1

    return render(request, "first_app/result.html")
def home(request):
    if "count" in request.session:
        request.session["count"] = 0 #why isn't this reseting the count?

    # if request.method = 'POST':
    return redirect ('/')



# Create your views here.
