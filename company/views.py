from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView

from infos.models import Lawsuit, News, Report

from .models import Company


class CompanyView(DetailView):
    template_name = "companies/company.html"
    model = Company

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context["score"] = self.get_object().compute_score()
        return context


def favorite_company(request: HttpRequest, company_id: int) -> HttpResponse:
    company = get_object_or_404(Company, pk=company_id)
    if company in request.user.favorite_companies.all():
        request.user.favorite_companies.remove(company)
    else:
        request.user.favorite_companies.add(company)
    return redirect("company:company", pk=company_id)


class InfosList(ListView):
    template_name = "companies/infos.html"
    model = None
    info_type = ""
    redirect_page = ""

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.company = get_object_or_404(Company, pk=kwargs.get("company_id"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "company": self.company,
                "info_type": self.info_type,
                "infos": self.model.objects.filter(company=self.company),
                "redirect_page": self.redirect_page,
            }
        )
        return context


class NewsList(InfosList):
    model = News
    info_type = "Notícias"
    redirect_page = "infos:newsdetail"


class ReportsList(InfosList):
    model = Report
    info_type = "Denúncias"
    redirect_page = "infos:reportdetail"

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context["infos"] = self.model.objects.filter(company=self.company, status="AP")
        return context


class LawsuitsList(InfosList):
    model = Lawsuit
    info_type = "Processos"
    redirect_page = "infos:lawsuitdetail"


class CompanyFormView(FormView):
    pass
