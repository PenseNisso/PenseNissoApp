from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from company.models import Company


class ComparatorView(View):
    def get(self, request):
        request.session["name"] = "comparator"
        selected_companies = get_selected_companies(request)

        selected_query = Company.objects.filter(name__in=selected_companies)
        context = {
            "name": request.session["name"],
            "companies": Company.objects.exclude(name__in=selected_companies),
            "selected_companies": selected_query,
        }
        return render(request, "comparator.html", context)

    def post(self, request):
        request.session["name"] = "comparator"
        selected_companies = get_selected_companies(request)

        if request.POST.get("company") not in selected_companies:
            selected_companies.append(request.POST.get("company"))
            request.session.modified = True

        selected_query = Company.objects.filter(name__in=selected_companies)

        context = {
            "name": request.session["name"],
            "companies": Company.objects.exclude(name__in=selected_companies),
            "selected_companies": selected_query,
        }
        return render(request, "comparator.html", context)


def delete(request):
    request.session["name"] = "comparator"
    selected_companies = get_selected_companies(request)

    company = request.GET.get("company")

    selected_companies.remove(company)
    request.session.modified = True

    return redirect("comparator:comparator")


def get_selected_companies(request):
    if "selected_companies" not in request.session:
        request.session["selected_companies"] = []

    return request.session["selected_companies"]
