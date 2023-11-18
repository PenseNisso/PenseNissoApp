from django.shortcuts import render
from django.views import View

# Create your views here.

class ComparatorView(View):
    def get(self, request):
        request.session["name"] = "comparator"
        context = {"name": request.session["name"]}
        return render(request, "comparator.html", context)
