# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
 
 
urlpatterns = [
    url(r'workspace/', include('project.urls')),
    
]
