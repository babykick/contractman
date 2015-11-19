# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
 
from .views import ProjectListView, ProjectFormView, ProjectDetailView, \
                   ContractFormView, ContractListView
 

urlpatterns = [
    url(r'^projects/$', ProjectListView.as_view(), name="projects"),
    url(r'^projects/add/$', ProjectFormView.as_view()),
    url(r'project/(?P<pk>[\w-]+)', ContractListView.as_view(), name="project"),
    url(r'project/(?P<pk>[\w-]+)/contracts', ContractListView.as_view(), name="contracts"),
]
