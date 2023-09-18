from django.contrib.auth import get_user
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from . import forms
from .models import Report


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
