#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-10-31 下午8:06
# @Author  : rhys
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from blog import feed
from blog.views import full_search
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^feed/', feed.LatestEntriesFeed(), name='feed'),
    url(r'^$', views.home, name='index'),
    url(r'^blog/(?P<slug>\S+)/$', views.detail, name='entry_detail'),
    url(r'^categories/', views.cat_view,  name='categories'),
    url(r'^tags/', views.tags_view, name='tags'),
    url(r'^about/', views.about_view, name='about'),

    url(r'^tag/(?P<tag_slug>\S+)/$', views.show_by_tag, name='show_by_tag'),
    url(r'^category/(?P<category_slug>\S+)/$', views.show_by_category, name='show_by_category'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.show_by_archive, name='show_by_archive'),

    url(r'^search/$', full_search, name='search'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
