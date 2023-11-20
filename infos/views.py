from typing import Any

from django.contrib.auth import get_user
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormView

from . import forms
from .models import Lawsuit, News, Report


class ReportSucessView(TemplateView):
    template_name = "confirmation.html"


class ReportFormView(FormView):
    template_name = "report.html"
    form_class = forms.ReportForm
    success_url = "confirmation/"

    def form_valid(self, form: forms.ReportForm) -> HttpResponse:
        data = form.cleaned_data
        current_date = timezone.now().isoformat(timespec="seconds")
        current_user = get_user(self.request)

        generated_title = (
            f"{current_date}-{data['company'].name}-{data['category'].name}"
        )

        report = Report(
            title=generated_title,
            content=data["description"],
            category=data["category"],
            links=data["link"],
            company=data["company"],
            user=current_user,
        )

        report.save()
        return super().form_valid(form)


class InfoDetails(DetailView):
    template_name = "info_details.html"
    info_title = None

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["info_title"] = self.info_title
        return context


class ReportDetails(InfoDetails):
    info_title = "Denúncia"
    model = Report

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['object'].links = context.get('object').links.split('\r\n')
        return context


class NewsDetails(InfoDetails):
    info_title = "Notícia"
    model = News


class LawsuitDetails(InfoDetails):
    info_title = "Processo"
    model = Lawsuit
