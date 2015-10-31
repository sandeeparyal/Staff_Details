from django.conf.urls import patterns, url

from kapra import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^letters/(?P<employee_id>\d+)$', views.letters, name='letters'),    
    url(r'(?P<word>\d+)/$', views.headsection_listings, name='headsection_listings'),
    url(r'(?P<hsection>\w+)$', views.section_listings, name='section_listings'),
    url(r'(?P<hsection>\w+)/(?P<section>\w+)/$', views.employee_listings, name='employee_listings'),

    )

