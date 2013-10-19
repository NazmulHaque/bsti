from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^officer$', views.officer, name='officer'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.home, name='home'),
)