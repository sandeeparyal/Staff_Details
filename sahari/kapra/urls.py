from django.conf.urls import patterns, url

from kapra import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^letters/$', views.letters, name='letters'),    
    url(r'(?P<word>\d+)/$', views.headsection_listings, name='headsection_listings'),
    url(r'(?P<hsection>\w+)$', views.section_listings, name='section_listings'),
    url(r'(?P<hsection>[\w\s]+)/(?P<section>[\w\s]+)/$', views.employee_listings, name='employee_listings'),
    )

