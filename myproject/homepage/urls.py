from django.urls import path, re_path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('articles/', views.articles, name='articles'),
    re_path(r'articles/(?P<year>[0-9]{4})/$',
            views.article_year, name='articles'),
]
