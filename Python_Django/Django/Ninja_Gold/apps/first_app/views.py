
from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime
from pytz import timezone

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'activity' in request.session:
        request.session['activity'] = []
    return render(request, "first_app/index.html")

def process_money(request):
    if request.POST['location'] == "Farm":
        goldFound = random.randrange(10,21)
        print goldFound, ":GOLD FOUND @ FARM"
        request.session['gold'] += goldFound
        print "TOTAL GOLD:", request.session['gold']
        request.session['activity'].insert(0, "Earned {} golds from the Farm! - {}".format(goldFound, datetime.now(timezone("US/Eastern")).strftime("%Y-%m-%d %H:%M:%S")))
        return redirect('/')
    elif request.POST['location'] == "Cave":
        goldFound = random.randrange(5,11)
        print goldFound, ":GOLD FOUND @ CAVE"
        request.session['gold'] += goldFound
        print "TOTAL GOLD:", request.session['gold']
        request.session['activity'].insert(0, "Earned {} golds from the Cave! - {}".format(goldFound, datetime.now(timezone("US/Eastern")).strftime("%Y-%m-%d %H:%M:%S")))
        return redirect('/')
    elif request.POST['location'] == "House":
        goldFound = random.randrange(2,51)
        print goldFound, ":GOLD FOUND @ HOUSE"
        request.session['gold'] += goldFound
        print "TOTAL GOLD:", request.session['gold']
        request.session['activity'].insert(0, "Earned {} golds from the House! - {}".format(goldFound, datetime.now(timezone("US/Eastern")).strftime("%Y-%m-%d %H:%M:%S")))
        return redirect('/')
    elif request.POST['location'] == "Casino":
        goldFound = random.randrange(-50,51)
        print goldFound, ":GOLD FOUND @ CASINO"
        request.session['gold'] += goldFound
        print "TOTAL GOLD:", request.session['gold']
        request.session['activity'].insert(0, "Earned {} golds from the Casino! - {}".format(goldFound, datetime.now(timezone("US/Eastern")).strftime("%Y-%m-%d %H:%M:%S")))
        return redirect('/')
def clearSession(request):
    request.session.clear()
    return redirect ('/')

# Create your views here.
