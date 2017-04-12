from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from table.views import FeedDataView
from .tables import ContactTable
from .models import Contact
from .forms import ContactDataForm


class HomePageView(TemplateView):
    template_name = 'contlog/home.html'
    contacts = ContactTable()
 

class EditContactView(UpdateView):
    model = Contact
    success_url = reverse_lazy('home')
    form_class = ContactDataForm
    #fields = ['name']
    template_name = 'contlog/edit_contact.html'
    now = timezone.now()

