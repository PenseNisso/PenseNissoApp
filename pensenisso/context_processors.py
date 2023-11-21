from django.http import HttpRequest

from company.models import Company


def get_company_suggestion(request: HttpRequest) -> dict:
    companies = Company.objects.all()
    return {"companies": companies}
