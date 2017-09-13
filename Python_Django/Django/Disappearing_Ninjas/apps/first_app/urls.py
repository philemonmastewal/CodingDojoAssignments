from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.allNinjas),
    url(r'^ninjas/(?P<ninja_color>\w+)$', views.ninjasColor)
]
