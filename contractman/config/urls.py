# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
from django.contrib import admin 
from project.views import IndexView, DashboardView
from company.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
     url(r'^logout/$', LogoutView.as_view(), name='loginout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('project.urls')),
    url(r'^accounts/login/$', LoginView.as_view()),
    url(r'^accounts/loginout/$', LogoutView.as_view() )
]
