from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from company.models import Company

from .trigram import TrigramSearch

MIN_SCORE = 2


class SearchView(ListView):
    model = Company
    template_name = "search.html"
    trigram = TrigramSearch(MIN_SCORE)

    def get_queryset(self, query):
        object_list = (
            Company.objects.filter(
                Q(name__icontains=query)
                | Q(
                    name__in=self.trigram.filter_set(
                        query, [company.name for company in Company.objects.all()]
                    )
                )
            )
            if query != None
            else None
        )
        return object_list

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        query = self.request.GET.get("search")
        self.object_list = self.get_queryset(query)
        context = super().get_context_data(**kwargs)
        context["query"] = query
        return super().render_to_response(context)
