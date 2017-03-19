# coding = utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Tag name',
        max_length=40
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name='Category name',
        max_length=200
    )

    slug = models.SlugField(
        verbose_name="Slug",
        help_text='Uri identifier.',
        unique=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class EntryManager(models.Manager):
    def published(self):
        return self.filter(is_published=True).filter(date_published__lte=timezone.now())


class Entry(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1024, null=True, blank=True)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=200, unique=True)
    is_published = models.BooleanField(default=True)
    is_recommend = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()

    recommend_degree = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    teaser = models.ImageField(upload_to="uploads/teaser", default='teaser/default.png')

    objects = EntryManager()

    def get_absolute_url(self):
        return reverse('blog:entry_detail', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ['-date_published']


class Comment(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    content = models.TextField()
    entry = models.ForeignKey(Entry)
