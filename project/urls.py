# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
 
from .views import ProjectListView, ProjectFormView, ProjectDetailView, \
                   ContractFormView, ContractListView
 

urlpatterns = [
    url(r'^projects/$', ProjectListView.as_view(), name="projects" ),
    url(r'^add/$', ContractFormView.as_view()),
    url(r'project/(?P<pk>[0-9]+)', ProjectDetailView.as_view(), name="project"),
]
