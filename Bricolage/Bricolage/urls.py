from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Bricolage.views.static.home', name='home'),
    url(r'^about/?$', 'Bricolage.views.static.about', name='about'),
    url(r'^coops/?$', 'Bricolage.views.static.coops', name='coops'),

    url(r'^admin/', include(admin.site.urls)),
)
