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
        queryset = queryset.filter(level='M')
        return queryset