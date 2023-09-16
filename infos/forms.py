from django import forms


class ReportForm(forms.Form):
    company_name = forms.CharField(label="Company", max_length=100)
    link = forms.URLField(label="Link")
    description = forms.CharField(label="Description", max_length=300)
    email = forms.EmailField(label="Email")
    contact_permission = forms.BooleanField()