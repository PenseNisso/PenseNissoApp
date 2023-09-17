from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from . import forms
from .models import Company, Report, ReportCategory


class ReportSucessView(TemplateView):
    template_name = "confirmation.html"


class ReportFormView(FormView):
    template_name = "report.html"
    form_class = forms.ReportForm
    success_url = "confirmation/"

    def form_valid(self, form) -> HttpResponse:
        data = form.cleaned_data
        queried_category = ReportCategory.objects.filter(name="categoria")
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

    def form_invalid(self, form) -> HttpResponse:
        errors = form.errors
        for i in errors:
            print(i)
        return super().form_invalid(form)
