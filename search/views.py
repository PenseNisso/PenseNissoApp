from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from company.models import Company
from .filters import BooleanFilter, TextFilter
from .forms import FilterForm


class SearchView(ListView):
    model = Company
    template_name = "search.html"


class QueryView(SearchView):
    def __init__(self, min_score: int = 2, **kwargs: Any) -> None:
        self.min_score = min_score
        super().__init__(**kwargs)

    def filter_set(self, keyword: str, set) -> "list[str]":
        filtered = []
        if keyword != None and keyword != "":
            for string in set:
                score = 0
                for i in range(len(keyword) - 2):
                    if keyword[i : i + 3] in string:
                        score += 1
                if score >= self.min_score:
                    filtered.append(string)
        return filtered

    def get_queryset(self, query):
        object_list = (
            Company.objects.filter(
                Q(name__icontains=query)
                | Q(
                    name__in=self.filter_set(
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


class ExplorerView(SearchView):
    template_name = "explorer.html"

    def apply_filters(self, filters):
        filter = Q()
        for applied_filter in filters:
            filter |= Q()
        return filter

    def build_filters(self, data: dict) -> "list[Q]":
        filters = []
        for d in data:
            if "has_report" in d:
                filters.append(BooleanFilter(type="num_reports", value=data[d]))
            elif "has_lawsuit" in d:
                filters.append(BooleanFilter(type="num_reports", value=data[d]))
            elif "has_news" in d:
                filters.append(BooleanFilter(type="num_reports", value=data[d]))
        return filters

    def get_queryset(self, filters):
        # object_list = Company.objects.filter(self.apply_filters(filters))
        object_list = Company.objects.all()
        print([company.reports.count() for company in Company.objects.all()])
        return object_list

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        self.form = FilterForm()
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        print(context.get('company_list')[0].reports)
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = FilterForm(request.GET)
        form.is_valid()
        self.object_list = self.get_queryset([])
        context = self.get_context_data(**kwargs)
        print(form.cleaned_data)
        return super().render_to_response(context)
