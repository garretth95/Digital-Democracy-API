from django.conf.urls import url
from django.contrib import admin
from . import views
from django.http import HttpResponseNotFound

app_name = 'DDAPIwebsite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_user/$', views.new_user, name='new_user'),
    url(r'^request_access/$', views.request_access, name='request_access'),
    url(r'^admin/', admin.site.urls),
    url(r'^test_get/', views.test_get, name='test_get'),
    url(r'^no_access/', views.no_access, name='no_access'),
    url(r'^hearing/(?P<hid>[0-9]+)/', views.hearing, name='hearing'),
    url(r'^service', views.service, name='service'),

]
