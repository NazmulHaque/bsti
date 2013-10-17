from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^officer', views.login, name='officer'),
    url(r'^$', views.home, name='home'),
)