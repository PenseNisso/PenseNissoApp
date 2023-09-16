from .models import Report, ReportCategory, Company

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from . import forms


class ReportSucessView(TemplateView):
    template_name = "confirmation.html"


class ReportFormView(FormView):
    template_name = "report.html"
    form_class = forms.ReportForm
    success_url = "confirmation/"

    def form_valid(self, form):
        data = form.cleaned_data
        category = ReportCategory(name="categoria")
        category.save()
        queried_category = ReportCategory.objects.filter(name="categoria")
        company = Company(name="Borin Inc")
        company.save()
        print(Company.objects.all())
        queried_company = Company.objects.get(pk=int(data["company_id"]))
        report = Report(
            title="titulo",
            content=data["description"],
            category=queried_category.get(),  # categoryId
            links=data["link"],
            company=queried_company,
            user=None,
            created_at="created_at",
            updated_at="updated_at",
        )

        report.save()

        return super().form_valid(form)
