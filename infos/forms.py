from django import forms
from django.forms import widgets

from company.models import Company

from .fields import CompanyModelChoiceField, ReportCategoryModelChoiceField
from .models import ReportCategory

STRING_COMPANY = "Empresa envolvida:"
STRING_EMPTY_COMPANY = "Selecione uma empresa"
STRING_LINK = "Links de evidências:"
STRING_DESCRIPTION = "Descrição da denúncia:"
STRING_CONTACT = "Podemos entrar em contato para obter mais informações?"
STRING_CATEGORY = "Escolha uma categoria de denúncia"
STRING_EMPTY_CATEGORY = "Selecione uma categoria"
STRING_DATE = "Data da ocorrência:"


class ReportForm(forms.Form):
    template_name = "form/report_form_template.html"

    company = CompanyModelChoiceField(
        queryset=Company.objects.all(),
        label=STRING_COMPANY,
        empty_label=STRING_EMPTY_COMPANY,
    )
    category = ReportCategoryModelChoiceField(
        queryset=ReportCategory.objects.all(),
        label=STRING_CATEGORY,
        empty_label=STRING_EMPTY_CATEGORY,
    )
    link = forms.URLField(label=STRING_LINK)
    description = forms.CharField(
        label=STRING_DESCRIPTION,
        max_length=300,
        widget=forms.Textarea(attrs={"cols": "45", "rows": "8"}),
    )
    date = forms.DateField(
        label=STRING_DATE, widget=widgets.DateInput(attrs={"type": "date"})
    )
    contact_permission = forms.BooleanField(
        label=STRING_CONTACT, required=False, initial=False
    )
