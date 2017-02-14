#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-10-31 下午8:06
# @Author  : rhys
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include

from blog import feed
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^feed/', feed.LatestEntriesFeed(), name='feed'),
    url(r'^$', views.home, name='index'),
    url(r'^blog/(?P<slug>\S+)/$', views.BlogDetail.as_view(), name='entry_detail'),
    url(r'^categories/', views.cat_view,  name='categories'),
    url(r'^tags/', views.tags_view, name='tags'),
    url(r'^about/', views.about_view, name='about'),
]