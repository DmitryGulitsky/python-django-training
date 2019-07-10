from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from django.http import HttpResponse

@require_http_methods(["GET", "POST"])
def index_page(request):
    if request.method == "GET":
        print("Method is GET")
    response = render(request, 'homepage/index.html')
    response['MyCustomHeader'] = 'spam-and-eggs'
    return response

@require_GET
def articles(request):
    my_obj = MyClass()
    my_obj.data = {'spam': 'eggs'}
    my_obj.list = list(range(10, 20))
    args = {
        'articles': list(range(1, 8)),
        # 'articles': [],
        'val0': '',
        'val1': '<h3>Value 1</h3>',
        'val2': '<h3>Value 2</h3>',
        'obj': my_obj
    }
    response = render(request, 'homepage/articles.html', args)
    return response

class MyClass:
    foo = 42
    bar = 60

    def __repr__(self):
        return f'<MyClass {self.foo} {self.bar}>'