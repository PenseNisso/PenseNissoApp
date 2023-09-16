
from django import forms


class ReportForm(forms.Form):
    company_id = forms.IntegerField(label="Company")
    link = forms.URLField(label="Link")
    description = forms.CharField(label="Description", max_length=300)
    # email = forms.EmailField(label="Email")
    contact_permission = forms.BooleanField()