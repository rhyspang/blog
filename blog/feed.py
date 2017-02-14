#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-11-1 下午8:48
# @Author  : rhys
# @File    : feed.py
# @Software: PyCharm
from django.contrib.syndication.views import Feed

from django.urls import reverse
from .models import Entry


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/feed/"
    description = "Updates on changes and additions to police beat central."


    def items(self):
        return Entry.objects.published()[:5]
