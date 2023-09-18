# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from .models import Company

# from infos.models import Lawsuit, News, Report

# Create your views here.


class ExplorerView(ListView):
    template_name = "companies/explorer.html"
    model = Company
    context_object_name = "companies"


class CompanyView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        context = {"company": company}
        return render(request, "companies/company.html", context)


class InfosView(View):
    template_name = "companies/infos.html"
    info_title = None
    model = None

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        infos = self.model.objects.filter(company__id=company_id)
        context = {
            "company": company,
            "info_title": self.info_title,
            "infos": infos,
        }
        return render(request, self.template_name, context)


# class NewsView(InfosView):
#     info_title = "Notícias"
#     model = News

# class ReportsView(InfosView):
#     info_title = "Denúncias"
#     model = Report

# class LawsuitsView(InfosView):
#     info_title = "Processos"
#     model = Lawsuit
