from .models import Report

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from . import forms


class ReportSucessView(TemplateView):
    template_name = "confirmation.html"


class ReportFormView(FormView):
    template_name = "report.html"
    success_url = "/report/success/"

    def form_valid(self, form):
        data = form.cleaned_data
        report = Report(
            "titulo",
            data["description"],
            "categoria 1", #categoryId
            data["link"], 
            data["company_id"], 
            #userId
            "created_at",
            "updated_at"
        )

        report.save()

        return super().form_valid(form)
