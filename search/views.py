from typing import Any

from django.db.models import Count, Q, Value
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from company.models import Company

from .filters import AbstractFilter, BooleanFilter, TextFilter
from .forms import FilterForm, SortingForm


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

    def apply_filters(self, filters: "list[AbstractFilter]"):
        filter = Q()
        for applied_filter in filters:
            filter &= applied_filter.get_q()
        return filter

    def build_filters(self, data: dict) -> "list[Q]":
        filters = []
        for d in data:
            if "has_report" in d:
                filters.append(BooleanFilter(type="reports", value=data[d]))
            elif "has_lawsuit" in d:
                filters.append(BooleanFilter(type="lawsuits", value=data[d]))
            elif "has_news" in d:
                filters.append(BooleanFilter(type="news", value=data[d]))
        return filters

    def apply_sorting(self, set, option: str):
        if option == "alphabetical_descending":
            set = set.order_by("-name")
        elif option == "most_reports":
            set = set.order_by("-count_reports")
        elif option == "least_reports":
            set = set.order_by("count_reports")
        elif option == "highest_score":
            set = sorted(set, key=lambda company: company.compute_score(), reverse=True)
        elif option == "lowest_score":
            set = sorted(set, key=lambda company: company.compute_score())
        else:
            set = set.order_by("name")
        return set

    def get_queryset(self, filters, sorting_option):
        object_list = (
            Company.objects.annotate(count_reports=Count("reports"))
            .annotate(count_lawsuits=Count("lawsuits"))
            .annotate(count_news=Count("news"))
            .filter(self.apply_filters(filters))
        )
        return self.apply_sorting(object_list, sorting_option)

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        self.form_filter = FilterForm()
        self.form_sorting = SortingForm()
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.form_filter
        context["form_sorting"] = self.form_sorting
        context["company_list"] = self.object_list
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form_filter = FilterForm(request.GET)
        form_sorting = SortingForm(request.GET)
        form_filter.is_valid()
        form_sorting.is_valid()
        filters = self.build_filters(form_filter.cleaned_data)
        self.object_list = self.get_queryset(
            filters=filters, sorting_option=form_sorting.cleaned_data["sorting"]
        )
        context = self.get_context_data(**kwargs)
        return super().render_to_response(context)