from django.conf.urls import patterns, include, url
from seguidor import views

urlpatterns = patterns(
    '',
    url(r'^seguidor/seguir/$', views.seguir, name='seguir')
)
