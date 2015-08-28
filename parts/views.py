from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from parts.models import Article


def list(request):
    articles = Article.objects.all().select_related('brand')
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render_to_response('parts_list.html', {'articles': articles})


def get(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('parts_get.html', {'article': article})