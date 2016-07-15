from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^', include('kapra.urls', namespace='karmachari')),
    url('', include('django.contrib.auth.urls')),
    url('^kapra/', include('kapra.urls', namespace='karmachari')),
    url(r'^admin/', include(admin.site.urls)),   
)
