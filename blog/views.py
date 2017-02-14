from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import generic

from blog.models import Entry, Tag
from . import models


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = 'blog/index.html'
    paginate_by = 2


def home(request):
    posts = models.Entry.objects.published()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'post_list': post_list})


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = 'blog/entry_detail.html'


def cat_view(request):
    cats = {}
    categories = models.Category.objects.all()
    for category in categories:
        cats[category.cat_name] = Entry.objects.filter(category=category)
    return render(request, 'blog/categories.html', {'cats': sorted(cats.items())})


def tags_view(request):
    tagsdict = {}
    tag_list = models.Tag.objects.all()
    for tag in tag_list:
        tagsdict[tag] = []

    for entry in Entry.objects.all():
        for tag in entry.tags.all():
            tagsdict[tag].append(entry)
    return render(request, 'blog/tags.html', {'tags': sorted(tagsdict.items(), key=lambda x: str(x[0]).lower())})


def about_view(request):
    return render(request, 'blog/about.html')
