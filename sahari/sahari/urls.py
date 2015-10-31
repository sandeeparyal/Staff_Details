from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'templates/base_site.html', name='index'),
    url('^kapra/', include('kapra.urls', namespace="kapra")),
    # Examples:
   # url(r'', include('views')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
