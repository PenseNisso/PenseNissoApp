from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from . import forms


class ReportSucessView(TemplateView):
    template_name = "confirmation.html"

class ReportFormView(FormView):
    template_name = "report.html"
    success_url = "/report/success/"
