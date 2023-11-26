from django.urls import path

from .views import (
    LawsuitStrategy,
    NewsStrategy,
    ReportStrategy,
    ReportFormView,
    ReportSucessView,
)

app_name = "infos"
urlpatterns = [
    path("report/confirmation/", ReportSucessView.as_view(), name="success"),
    path("report/", ReportFormView.as_view(), name="report"),
    path("denuncia/<int:pk>", ReportStrategy.as_view(), name="reportdetail"),
    path("noticia/<int:pk>", NewsStrategy.as_view(), name="newsdetail"),
    path("processo/<int:pk>", LawsuitStrategy.as_view(), name="lawsuitdetail"),
]
