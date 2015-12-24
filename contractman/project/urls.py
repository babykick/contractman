# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
 
from .views import DashboardView, ProjectListView, ProjectFormView, ProjectDetailView, \
                   ContractCreateView, ContractListView, ContractDetailView
from company.views import MemberView
 


# Contracts under the project
contracts_pattern = [  url(r'^contracts/add/$', ContractCreateView.as_view(), name="addcontract"),
                       url(r'^contracts/$', ContractListView.as_view(), name="contracts"),   
                     ]


# Project
urlpatterns = [
    # 工作台
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    # 项目列表
    url(r'^projects/$', ProjectListView.as_view(), name="projects"),
    # 项目详情
    url(r'^project/(?P<pk>[\w-]+)/$', ProjectDetailView.as_view(), name='project'),
    # 增加项目
    url(r'^projects/add/$', ProjectFormView.as_view(), name="addproject"),
    # 合同url集合 
    url(r'^project/(?P<pk>[\w-]+)/', include(contracts_pattern)),
    # 合同详细
    url(r'^contract/(?P<pk>[\w-]+)/', ContractDetailView.as_view(), name='contract_detail'),
    # 成员
    url(r'^member/(?P<pk>[0-9]+)/$', MemberView.as_view(), name='member'), 
]