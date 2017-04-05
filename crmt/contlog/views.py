from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Contact

class HomePageView(ListView):
    model = Contact
    context_object_name = 'allcontacts'
    template_name = 'contlog/home.html'
    paginate_by = 10

    def get_queryset(self):
        #добавить сюда последнее событие
        name_val = self.request.GET.get('name', '')
        if name_val:
            new_qs = Contact.objects.filter(name__icontains=name_val)#.order_by(order)
        else:
            new_qs = Contact.objects.all()
        return new_qs

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        # paginator = Paginator(self.get_queryset(), self.paginate_by)
        # page = self.request.GET.get('page')
        # try:
        #     allcontacts = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     allcontacts = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     allcontacts = paginator.page(paginator.num_pages)
        # context['allcontacts'] = allcontacts

        context['name'] = self.request.GET.get('name', '')
        
        #context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        return context



