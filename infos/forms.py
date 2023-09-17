from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList

STRING_COMPANY = "Empresa envolvida:"
STRING_LINK = "Links de evidências:"
STRING_DESCRIPTION = "Descrição da denúncia:"
STRING_CONTACT = "Podemos entrar em contato para obter mais informações?"

class ReportForm(forms.Form):
    template_name = "form/report_form_template.html"

    company_id = forms.IntegerField(label=STRING_COMPANY)
    link = forms.URLField(label=STRING_LINK)
    description = forms.CharField(label=STRING_DESCRIPTION, max_length=300)
    contact_permission = forms.BooleanField(label=STRING_CONTACT, required=False)
    # email = forms.EmailField(label="Email")