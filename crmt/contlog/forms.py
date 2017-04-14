from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from .models import Contact
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Button
from crispy_forms.bootstrap import FormActions, PrependedText


class ContactDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True

    class Meta:
        model = Contact
        fields = '__all__'
        
        
                     