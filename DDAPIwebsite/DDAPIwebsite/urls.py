from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'DDAPIwebsite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^request_access/$', views.request_access, name='request_access'),
    url(r'^admin/', admin.site.urls),
]
