from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from .models import Entry, Tag, Category, Comment


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_published')
    prepopulated_fields = {'slug': ('title',)}
    body = forms.CharField(widget=CKEditorWidget())


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
