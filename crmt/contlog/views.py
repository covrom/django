from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Contact
from .forms import ContactDataForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class HomePageView(TemplateView):
    template_name = 'contlog/home.html'
 
class ContactsView(TemplateView):
    template_name = 'contlog/contacts.html'
    contacts = Contact.objects.all() #view.contacts
    
    def get(self, request, *args, **kwargs):
        self.paginator = Paginator(self.contacts, 10)
        page = request.GET.get('page')
        try:
            self.contacts = self.paginator.page(page)
            self.number = int(page)
        except PageNotAnInteger:
            self.number = 1
            self.contacts = self.paginator.page(self.number)
        except EmptyPage:
            self.number = self.paginator.num_pages
            self.contacts = self.paginator.page(self.number)
        return super(ContactsView, self).get(request, *args, **kwargs)

class EditContactView(UpdateView):
    model = Contact
    success_url = reverse_lazy('home')
    form_class = ContactDataForm
    #fields = ['name']
    template_name = 'contlog/edit_contact.html'
    now = timezone.now()

def contact_create(request):
    """Обрабатывает ajax запросы для формы ввода нового контакта"""
    data = {}
    if request.method == 'POST':
        form = ContactDataForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ContactDataForm()
    context = {'form': form}
    data['html_form'] = render_to_string('contlog/part_cont_create.html',
        context,
        request=request
    )
    return JsonResponse(data)
