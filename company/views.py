# Create your views here.
from django.shortcuts import get_object_or_404, render

from .models import Company
from infos.models import Lawsuit, News, Report

# Create your views here.

def explorer(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'companies/explorer.html', context)

def company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    context = {
        'company': company
    }
    return render(request, 'companies/company.html', context)

def news(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    news = News.objects.filter(company__id = company_id)
    context = {
        'company': company,
        'info_title': "Notícias",
        'infos': news,
    }
    return render(request, 'companies/infos.html', context)

def reports(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    reports = Report.objects.filter(company__id = company_id)
    print(reports)
    context = {
        'company': company,
        'info_title': "Denúncias",
        'infos': reports,
    }
    return render(request, 'companies/infos.html', context)

def lawsuits(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    lawsuits = Lawsuit.objects.filter(company__id = company_id)
    context = {
        'company': company,
        'info_title': "Processos",
        'infos': lawsuits,
    }
    return render(request, 'companies/infos.html', context)
