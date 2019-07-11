from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from random import randint


class IndexPageView(TemplateView):
    template_name = 'homepage/index.html'

    def get(self, request):
        return render(request, self.template_name)


class ArticleView(TemplateView):
    template_name = 'homepage/articles.html'

    def get_date_list(self, count=10):
        result = []
        today = datetime.today()
        for i in range(count):
            date = today - timedelta(days=i)
            for j in range(randint(1, 4)):
                result.append(
                    date.replace(hour=randint(0, 23))
                )
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_obj = MyClass()
        my_obj.data = {'spam': 'eggs'}
        my_obj.list = list(range(10, 20))
        my_obj.baz = list(range(7))
        args = {
            'articles': list(range(1, 8)),
            # 'articles': [],
            'val0': '',
            'val1': 'OTUS',
            'val2': '<h3>Value 2</h3>',
            'obj': my_obj,
            'a_title': 'django and sublime text 3',
            'string': ('First line\n'
                       'Second line\n'
                       'Third line\n'
                       ),
            'current': datetime.today(),
            'dates': self.get_date_list(),
            'items': list(range(4, ))
        }
        context.update(args)
        return context


def article_year(request, year):
    return HttpResponse(f'<h1>Year is {year}</h1>')


class MyClass:
    foo = 42
    bar = 60

    def __repr__(self):
        return f'<MyClass {self.foo} {self.bar}>'
