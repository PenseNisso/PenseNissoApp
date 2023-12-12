from typing import Any

from django.contrib.auth import get_user
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView, TemplateView

from infos.models import Lawsuit, News, Report

from .forms import CompanySuggestion
from .models import Company, CompanySuggestionModel, Rate 


class CompanyView(DetailView):
    template_name = "companies/company.html"
    model = Company

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        object = self.get_object()

        rates = object.user_ratings.all()
        user_ratings = []
        for rate in rates:
            user_ratings.append(rate.user)

        context["user_ratings"] = user_ratings
        context["score_users"] = object.compute_score_users()
        context["score"] = object.compute_score()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        query = self.request.POST.get("rate")
        context = self.get_context_data(**kwargs)
        print(request.user)
        rate = Rate(company=context["company"], user=request.user, score=int(query))
        
        rate.save()
        return super().render_to_response(self.get_context_data(**kwargs))


def change_rate(request: HttpRequest, company_id: int) -> HttpResponse:
    company = get_object_or_404(Company, pk=company_id)
    rates = company.user_ratings.filter(user=request.user)
    rates.delete()

    return redirect("company:company", pk=company_id)

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


class SuggestionSucessView(TemplateView):
    template_name = "companies/forms/confirmation.html"


class CompanyFormView(FormView):
    form_class = CompanySuggestion
    success_url = "suggest/confirmation"
    template_name = "companies/forms/company_suggestion.html"

    def form_valid(self, form: CompanySuggestion) -> HttpResponse:
        data = form.cleaned_data
        current_user = get_user(self.request)
        suggestion = CompanySuggestionModel(
            name=data["name"],
            field_of_operation=data["field_of_operation"],
            description=data["description"],
            link=data["link"],
            user=current_user if current_user.is_authenticated else None,
        )

        suggestion.save()
        return super().form_valid(form)
