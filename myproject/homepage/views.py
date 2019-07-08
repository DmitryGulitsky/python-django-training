from django.shortcuts import render

from django.http import HttpResponse


def index_page(request):
    response = HttpResponse('<h1>Welcome to index of Homepage!</h1>')
    response['MyCustomHeader'] = 'spam-and-eggs'
    return response
