from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^projects$', views.projects, name = 'projects'),
    url(r'^about$', views.about, name ='about'),
    url(r'^testimonials$', views.testimonials, name = 'testimonials'),
    url(r'^new_user$', views.create)
]
