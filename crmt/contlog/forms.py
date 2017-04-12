from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from .models import Contact
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Button
from crispy_forms.bootstrap import FormActions, PrependedText


class ContactDataForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactDataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-contact-data-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
            'name','places',
            Div(PrependedText('email', '@', placeholder="Email")),
            'phones', css_class = 'container'
            ),
            TabHolder(Tab('Реквизиты', 'requisites', css_id='reqs'),
                     Tab('Заметки', 'comments', css_id='comm')
                     ),
            FormActions(Submit('save', 'Записать'), Button('cancel', 'Отмена', onclick='location.reload();'))
            
            )

    class Meta:
        model = Contact
        fields = (
          "name",
          "places",
          "phones",
          "email",
          "requisites",
          "comments",
        )
                     