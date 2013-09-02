from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #admin
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^officer/', include('officers.urls')),
    url(r'^', include('users.urls')),
    # url(r'^bsti/', include('bsti.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)