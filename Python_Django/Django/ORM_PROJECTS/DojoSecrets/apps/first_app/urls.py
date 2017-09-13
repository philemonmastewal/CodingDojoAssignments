from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^registration$', views.registration),
    url(r'^secrets$', views.secrets),
    url(r'^popular_secrets$', views.popular_secrets),
    url(r'^process_like/(?P<secret_id>\d+)$', views.process_like),

]
