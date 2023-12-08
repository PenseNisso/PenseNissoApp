from django.urls import path

from .views import (CompanyView, LawsuitsList, NewsList, ReportsList,
                    favorite_company)

app_name = "company"
urlpatterns = [
    path("<int:pk>/", CompanyView.as_view(), name="company"),
    path("<int:company_id>/favoritar", favorite_company, name="favorite"),
    path("<int:company_id>/noticias", NewsList.as_view(), name="news"),
    path("<int:company_id>/processos", LawsuitsList.as_view(), name="lawsuits"),
    path("<int:company_id>/denuncias", ReportsList.as_view(), name="reports"),
]
