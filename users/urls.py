from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home')
    # url(r'^officer/', views.index, name='index')
)