from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^kapra/', include('kapra.urls', namespace='kapra')),
    url(r'^admin/', include(admin.site.urls)),
)
