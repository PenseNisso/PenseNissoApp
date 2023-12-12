from django.urls import path

from .views import (
    CompanyView,
    LawsuitsList,
    NewsList,
    ReportsList,
    change_rate,
    favorite_company,
    SuggestionSucessView,
)

app_name = "company"
urlpatterns = [
    path("<int:pk>/", CompanyView.as_view(), name="company"),
    path("<int:company_id>/change", change_rate, name="change"),
    path("<int:company_id>/favoritar", favorite_company, name="favorite"),
    path("<int:company_id>/noticias", NewsList.as_view(), name="news"),
    path("<int:company_id>/processos", LawsuitsList.as_view(), name="lawsuits"),
    path("<int:company_id>/denuncias", ReportsList.as_view(), name="reports"),
    path("suggest", CompanyFormView.as_view(), name="suggest"),
    path(
        "suggest/confirmation", SuggestionSucessView.as_view(), name="suggest_success"
    ),
]
