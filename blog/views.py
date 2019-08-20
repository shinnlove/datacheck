from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def hello_world(requset):
    return HttpResponse("hello world")

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id=article.article_id
    publish_date = article.publish_date
    return HttpResponse(title+"test"+brief_content)

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')


@csrf_exempt
def all(request):
    if request.method == 'GET':
        pageSize = int(request.GET.get('pageSize'))
        pageNumber = int(request.GET.get('pageNumber'))
        searchText = request.GET.get('searchText')
        sortName = request.GET.get('sortName')
        sortOrder = request.GET.get('sortOrder')

    total = Article.objects.all().count()
    articles = Article.objects.order_by('article_id')[(pageNumber - 1) * pageSize:(pageNumber) * pageSize]
    rows = []
    data = {"total": total, "rows": rows}
    for article in articles:
        rows.append({'id': article.article_id, 'title': article.title, 'content': article.brief_content})

    return HttpResponse(json.dumps(data), content_type="application/json")


def add(request):
    return render(request, 'add.html')


@csrf_exempt
def deal(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        ret = {"ret": 0, 'title': title, 'content': content}
        return HttpResponse(json.dumps(ret))


def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'article.html', {'article': article})


def get_an_apple(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def delete(request):
    return_dict = {"ret": True, "errMsg": "", "rows": [], "total": 0}
    article_id = request.POST.get('id')
    article = Article.objects.get(id=article_id)
    article.delete()
    return HttpResponse(json.dumps(return_dict))