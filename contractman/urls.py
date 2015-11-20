# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
from django.contrib import admin 
from project.views import IndexView
from company.views import LoginView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('project.urls')),
    url(r'^accounts/login/$', LoginView.as_view() )
]
