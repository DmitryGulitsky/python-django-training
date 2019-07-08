from django.shortcuts import render

from django.http import HttpResponse


def index_page(request):
    response = render(request, 'homepage/index.html')
    response['MyCustomHeader'] = 'spam-and-eggs'
    return response

def articles(request):
    return HttpResponse('Articles')