from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from .models import Entry, Tag, Category, Comment


#
# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Entry


# class PostAmin(admin.ModelAdmin):
#     form = PostAdminForm


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_published')
    prepopulated_fields = {'slug': ('title',)}
    body = forms.CharField(widget=CKEditorWidget())


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)