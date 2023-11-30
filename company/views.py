from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from infos.models import News, Report

from .models import Company


class ExplorerView(ListView):
    template_name = "companies/explorer.html"
    model = Company
    context_object_name = "companies"


class CompanyView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        context = {"company": company}
        return render(request, "companies/company.html", context)


class InfosList(View):
    template_name = "companies/infos.html"
    model = None
    info_type = ""
    redirect_page = ""

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        infos = self.model.objects.filter(company__id=company_id)
        context = {
            "company": company,
            "info_type": self.info_type,
            "infos": infos,
            "redirect_page": self.redirect_page,
        }
        return render(request, self.template_name, context)


class NewsList(InfosList):
    info_title = "Notícias"
    model = News
    redirect_page = "infos:newsdetail"


class ReportsList(InfosList):
    model = Report
    info_type = "Denúncias"
    redirect_page = "infos:reportdetail"


# class LawsuitsView(InfosView):
#     info_title = "Processos"
#     model = Lawsuit
