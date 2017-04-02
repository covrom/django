from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Contact

class HomePageView(ListView):
    model = Contact
    context_object_name = 'allcontacts'
    #добавить сюда последнее событие
    queryset = Contact.objects.all()
    template_name = 'contlog/home.html'



