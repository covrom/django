from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# from table.views import FeedDataView
# from .tables import ContactTable
from .models import Contact
from .forms import ContactDataForm
from django.http import JsonResponse
from django.template.loader import render_to_string


class HomePageView(TemplateView):
    template_name = 'contlog/home.html'
 
class ContactsView(TemplateView):
    template_name = 'contlog/contacts.html'
    # contacts = ContactTable()
    contacts = Contact.objects.all() #view.contacts

class EditContactView(UpdateView):
    model = Contact
    success_url = reverse_lazy('home')
    form_class = ContactDataForm
    #fields = ['name']
    template_name = 'contlog/edit_contact.html'
    now = timezone.now()

def contact_create(request):

    data = {}

    if request.method == 'POST':
        form = ContactDataForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            cnts = Contact.objects.all()
            data['html_cnt_list'] = render_to_string('contlog/part_cont_list.html', {
                'view': {'contacts':cnts}
            })
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
