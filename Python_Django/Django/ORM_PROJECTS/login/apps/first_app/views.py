from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from .models import User

def index(request):
  print("Running index method, calling out to User.")
  user = User.Manager.login("philemonmastewal@gmail.com","Password")
# DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
  print (type(user))
  if 'error' in user:
      pass
  if 'theuser' in user:
      pass
  return HttpResponse("Done running userManager method. Check your terminal console.")
