# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
 
from .views import DashboardView, ProjectListView, ProjectFormView, ProjectDetailView, \
                   ContractFormView, ContractListView
from company.views import MemberView
 


# Contracts under the project        
contracts_pattern = [  url(r'^add/$', ContractFormView.as_view(), name="addcontract"),
                          
                     ]


# Project
urlpatterns = [
    # dashboard
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    # project list
    url(r'^projects/$', ProjectListView.as_view(), name="projects"),
    # project detail
    url(r'^project/(?P<pk>[\w-]+)/$', ProjectDetailView.as_view(), name='project'),
    # add project
    url(r'^projects/add/$', ProjectFormView.as_view(), name="addproject"),
    
    url(r'^member/(?P<pk>[0-9]+)/$', MemberView.as_view(), name='member'), 
    url(r'^project/(?P<pk>[\w-]+)/', include(contracts_pattern)),
    
]