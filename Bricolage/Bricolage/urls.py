from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Bricolage.views.static.home', name='home'),
    url(r'^home/?$', 'Bricolage.views.static.home'),
    url(r'^index/?$', 'Bricolage.views.static.home'),

    url(r'^about/?$', 'Bricolage.views.static.about', name='about'),
    url(r'^coops/?$', 'Bricolage.views.static.coops', name='coops'),
    url(r'^more/?$', 'Bricolage.views.static.more', name='more'),
    url(r'^faq/?$', 'Bricolage.views.static.faq', name='faq'),

    url(r'^admin/', include(admin.site.urls)),
)
