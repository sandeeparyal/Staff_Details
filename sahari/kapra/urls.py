# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from kapra import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'hs(?P<ministry_id>\d+)/$', views.headsection_listings, name='headsection_listings'),
    url(r's(?P<ministry_id>\d+)/(?P<head_section_id>\d+)/$', views.section_listings, name='section_listings'),
    url(r'e(?P<ministry_id>\d+)/(?P<head_section_id>\d+)/(?P<section_id>\d+)/$', views.employee_listings, name='employee_listings'),
    )

