from django.urls import path, re_path, register_converter
from django.views.generic import TemplateView

from . import views

app_name = 'homepage'

class YearConverter:
    regex = r'[0-9]{4}'

    def to_python(self, value):
        value = int(value)
        return value

    def to_url(self, value):
        if value < 2000:
            raise ValueError
        return '%04d' % value


register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.TemplateView.as_view(
        template_name='homepage/index.html'),
         name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/<year:year>', views.article_year, name='articles_year'),
    #re_path(r'articles/(?P<year>[0-9]{4})/$',
    #        views.article_year, name='articles'),
]
