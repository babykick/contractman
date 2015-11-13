# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
 
from .views import ProjectListView, ProjectFormView, \
                   ContractFormView, ContractListView
 

urlpatterns = [
    url(r'^projects/$', ProjectListView.as_view(), name='project_list'),
    url(r'^add/$', ContractFormView.as_view()),
]
