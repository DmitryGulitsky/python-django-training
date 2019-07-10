from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from django.http import HttpResponse
from datetime import datetime, timedelta
from random import randint


@require_http_methods(["GET", "POST"])
def index_page(request):
    if request.method == "GET":
        print("Method is GET")
    response = render(request, 'homepage/index.html')
    response['MyCustomHeader'] = 'spam-and-eggs'
    return response


def get_date_list(count=10):
    result = []
    today = datetime.today()
    for i in range(count):
        date = today - timedelta(days=i)
        for j in range(randint(1, 4)):
            result.append(
                date.replace(hour=randint(0, 23))
            )
    return result


@require_GET
def articles(request):
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
        'dates': get_date_list(),
        'items': list(range(4,))
    }
    print(get_date_list())
    response = render(request, 'homepage/articles.html', args)
    return response


class MyClass:
    foo = 42
    bar = 60

    def __repr__(self):
        return f'<MyClass {self.foo} {self.bar}>'
