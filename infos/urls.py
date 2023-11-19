from django.urls import path

from .views import (
    LawsuitDetails,
    NewsDetails,
    ReportDetails,
    ReportFormView,
    ReportSucessView,
)

app_name = "infos"
urlpatterns = [
    path("report/confirmation/", ReportSucessView.as_view(), name="success"),
    path("report/", ReportFormView.as_view(), name="report"),
    path("denuncia/<int:pk>", ReportDetails.as_view(), name="reportdetail"),
    path("noticia/<int:pk>", NewsDetails.as_view(), name="newsdetail"),
    path("processo/<int:pk>", LawsuitDetails.as_view(), name="lawsuitdetail"),
]
