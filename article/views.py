from django.shortcuts import render
from .models import Category, Article
from django.http import HttpResponse

def index(request):
    category = Category(name='最新文章')
    category.save()
    article = Article(title='三国', comtent='2323')
    article.category = category
    article.save()
    return HttpResponse('SUCCESS')
