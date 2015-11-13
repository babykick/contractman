# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
from django.contrib import admin 
from project.views import IndexView
 
urlpatterns = [
    url(r'^$', IndexView.as_view(),  name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^workspace/', include('project.urls')),
]
