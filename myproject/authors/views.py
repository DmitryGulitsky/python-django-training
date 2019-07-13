from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import AuthorsModel

# Create your views here.


class IndexView(ListView):

    model = AuthorsModel
    template_name = 'authors/index.html'
    context_object_name = 'authors'

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['authors'] = AuthorsModel.objects.all()
    #    return context

    def get_queryset(self):
        queryset = super().get_queryset()
        # __gt means greater than
        # queryset = queryset.filter(id__gt=1)
        # __endswith means item value in the end
        # queryset = queryset.filter(email__endswith='otus.ru')
        return queryset