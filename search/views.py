from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from company.models import Company


class SearchView(ListView):
    model = Company
    template_name = "search.html"

    def get_queryset(self, query):
        object_list = (
            Company.objects.filter(Q(name__icontains=query)) if query != None else None
        )
        return object_list

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        query = self.request.GET.get("search")
        self.object_list = self.get_queryset(query)
        context = super().get_context_data(**kwargs)
        context["query"] = query
        return super().render_to_response(context)
