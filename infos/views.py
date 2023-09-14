from django.shortcuts import get_object_or_404, render

from infos.models import Company

# Create your views here.

def explorer(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'explorador.html', context)

def company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    context = {
        'company': company
    }
    return render(request, 'companies/company.html', context)
