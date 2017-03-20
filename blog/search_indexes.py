# -*- coding: utf-8 -*-
from blog.models import Entry
from haystack import indexes


class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content = indexes.CharField(model_attr='body')
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Entry

    def index_queryset(self, using=None):
        return self.get_model().objects.published()

