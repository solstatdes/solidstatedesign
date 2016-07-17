
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'tmm.views.homeOptics', name='optic-home'),
    url(r'^app$', 'tmm.views.home', name='optic-app'),
    url(r'^save_project/$', 'tmm.views.save_project', name='save_project'),
    url(r'^lib_page/$', 'tmm.views.lib_page', name='lib_page'),
    url(r'^add_layer/$', 'tmm.views.add_layer', name='add_layer'),
)
