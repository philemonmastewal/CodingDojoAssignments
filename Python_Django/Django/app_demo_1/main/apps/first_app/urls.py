from django.conf.urls import url  #this gives us access to the function 'url'
from . import views #This gives us access to everything (.) in a 'views.py' file that Django automatically created for us when we built our first_app. This views file doesn't do anything, yet. We'll add code soon.

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.show)
]
