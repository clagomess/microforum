from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns(
    '',
    url(r'^test$', views.test, name='test'),
    url(r'^test_json', views.test_json, name='test_json'),
    url('', include('webview.urls')),
    url('', include('seguidor.urls'))
)
