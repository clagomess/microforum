from django.conf.urls import patterns, url
from webview import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^post/(?P<cod_post>[a-zA-Z0-9]+)$', views.post, name='post'),
    url(r'^profile/(?P<cod_usuario>[a-zA-Z0-9]+)$', views.profile, name='profile'),
    url(r'^config/$', views.config, name='config'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^upload$', views.upload, name='upload')
)
