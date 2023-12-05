from django.shortcuts import render
from django.views import View

from company.models import Company

class ComparatorView(View):
    def get(self, request):
        request.session["name"] = "comparator"
        request.session["selected_companies"] = []
        context = {"name": request.session["name"],
                   "companies": Company.objects.all(),
                   "selected_companies": request.session["selected_companies"]
                  }
        return render(request, "comparator.html", context)
    def post(self, request):
        request.session["selected_companies"].append(request.POST.get("company"))
        request.session.modified = True
        #request.session["selected_companies"].append(Company.objects.filter(name = request.POST.get("company")))
        selected_query = Company.objects.filter(name__in = request.session["selected_companies"])
        print(selected_query)
        print(request.session["selected_companies"])
        context = {"name": request.session["name"],
                   "companies": Company.objects.exclude(name__in = request.session["selected_companies"]),
                   "selected_companies": selected_query
                  }
        return render(request, "comparator.html", context)
