# coding = utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.slug


class Category(models.Model):
    cat_name = models.CharField(
        verbose_name='Category name',
        max_length=200
    )

    slug = models.SlugField(
        verbose_name="Slug",
        help_text='Uri identifier.',
        unique=True
    )

    def __unicode__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        app_label = 'blog'
        ordering = ['cat_name']


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    # body = models.TextField()
    body = RichTextUploadingField()
    # body = UEditorField(u'content', width=600, height=300, toolbars="full", imagePath="", filePath="",
    #                     upload_settings={"imageMaxSize": 1204000},
    #                     settings={}, command=None, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    teaser = models.ImageField(upload_to="upload/teaser")

    objects = EntryQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('blog:entry_detail', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ['-created']
