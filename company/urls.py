from django.urls import path

from .views import CompanyView, ExplorerView, ReportsList

app_name = "company"
urlpatterns = [
    path("", ExplorerView.as_view(), name="explorer"),
    path("<int:company_id>/", CompanyView.as_view(), name="company"),
    # path('<int:company_id>/noticias/',NewsView.as_view(), name="news"),
    # path('<int:company_id>/processos/',LawsuitsView.as_view(), name="lawsuits"),
    path("<int:company_id>/denuncias", ReportsList.as_view(), name="reports"),
]
