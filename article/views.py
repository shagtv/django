from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.core import serializers

from article.models import Article


def basic_one(request):
    view = "basic_one"
    html = "<html><head></head><body>This is %s view!</body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "basic_two"
    t = get_template('myview.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_three(request):
    view = "basic_three"
    return render_to_response('myview.html', {'name': view})

def list(request):
    return render_to_response('list.twig', {'articles': Article.objects.all()})

def json(request):
    data = serializers.serialize("json", Article.objects.all())
    return HttpResponse(data, content_type='application/json')