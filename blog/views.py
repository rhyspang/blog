from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views import generic
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from blog.models import Entry, Tag, Category
from . import models
from django.conf import settings


def global_settings(request):
    posts = Entry.objects.published()
    archives_list = archives(posts)
    tags_list = Tag.objects.all()
    categories_list = Category.objects.all()
    top_three = Entry.objects.published()[:3]
    return dict(settings.WEB_INFO, **locals())


def paginate(request, article_list):
    paginator = Paginator(article_list, 8)
    page = request.GET.get('page')
    try:
        page_list = paginator.page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return page_list


def archives(articles):
    archives_list = []
    date_list = articles.dates('date_published', 'month', order='DESC')
    for date in date_list:
        archives_list.append((date.year, date.month))
    return archives_list


def home(request):
    posts = Entry.objects.published()
    articles_list = paginate(request, posts)
    return render(request, 'blog/index.html', locals())


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = 'blog/entry_detail.html'


def detail(request, slug):
    article = get_object_or_404(Entry, slug=slug)
    article.click_count += 1
    article.save()
    return render(request, 'blog/entry_detail.html', locals())


def cat_view(request):
    cats = {}
    categories = Category.objects.all()
    for category in categories:
        cats[category.name] = Entry.objects.published().filter(category=category)
    return render(request, 'blog/categories.html', {'cats': sorted(cats.items())})


def tags_view(request):
    tagsdict = {}
    tag_list = Tag.objects.all()
    for tag in tag_list:
        tagsdict[tag] = []

    for entry in Entry.objects.published():
        for tag in entry.tags.all():
            tagsdict[tag].append(entry)
    return render(request, 'blog/tags.html', {'tags': sorted(tagsdict.items(), key=lambda x: str(x[0]).lower())})


def about_view(request):
    return render(request, 'blog/about.html')


def show_by_tag(request, tag_slug):
    articles_list = Entry.objects.published().filter(tags__slug__exact=tag_slug)
    articles_list = paginate(request, articles_list)
    return render(request, 'blog/show_by_tag.html', locals())


def show_by_archive(request, year, month):
    articles_list = Entry.objects.published() \
        .filter(date_published__year=year) \
        .filter(date_published__month=month)
    articles_list = paginate(request, articles_list)
    return render(request, 'blog/show_by_archive.html', locals())


def show_by_category(request, category_slug):
    articles_list = Entry.objects.published().filter(category__slug=category_slug)
    articles_list = paginate(request, articles_list)
    return render(request, 'blog/show_by_category.html', locals())


def full_search(request):
    form = SearchForm(request.GET)
    keywords = request.GET['q']
    articles_list = []
    search_result = form.search()
    for item in search_result:
        articles_list.append(item.object)
    return render(request, 'blog/search_result.html', locals())

