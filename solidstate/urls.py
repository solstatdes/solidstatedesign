from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'solidstate.views.home', name='home'),
    url(r'^optics/', include('tmm.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^idea/accounts/', include('allauth.urls'))
)
