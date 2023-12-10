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
            user=current_user if current_user.is_authenticated else None,
            date=data["date"],
        )

        report.save()
        return super().form_valid(form)


class InfoStrategy(DetailView):
    info_type = ""

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context.update(
            {"info_type": self.info_type, "info_title": self.get_info_title()}
        )
        return context

    def get_info_title(self):
        pass


class ReportStrategy(InfoStrategy):
    model = Report
    info_type = "Denúncia"
    template_name = "report_details.html"

    def get_info_title(self):
        return self.get_object().category

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context["object"].links = context.get("object").links.split("\r\n")
        return context


class NewsStrategy(InfoStrategy):
    model = News
    info_type = "Notícia"
    template_name = "news_details.html"

    def get_info_title(self):
        return self.get_object().title


class LawsuitStrategy(InfoStrategy):
    model = Lawsuit
    info_type = "Processo"
    template_name = "lawsuit_details.html"

    def get_info_title(self):
        return self.get_object().title
