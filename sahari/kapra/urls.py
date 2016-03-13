# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from kapra import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<ministry_id>\d+)/$', views.headsection_listings, name='headsection_listings'),
    url(r'(?P<hsection_id>\d+)/$', views.section_listings, name='section_listings'),
    url(r'(?P<headsection_id>\d+)/(?P<section_id>\d+)/$', views.employee_listings, name='employee_listings'),
    )

