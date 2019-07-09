from django.shortcuts import render

from django.http import HttpResponse


def index_page(request):
    response = render(request, 'homepage/index.html')
    response['MyCustomHeader'] = 'spam-and-eggs'
    return response

def articles(request):
    args = {
        'articles': list(range(1, 8))
    }
    response = render(request, 'homepage/articles.html', args)
    return response