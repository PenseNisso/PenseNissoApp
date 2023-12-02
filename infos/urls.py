from django.urls import path

from . import views

app_name = "infos"
urlpatterns = [
    path("report/confirmation/", views.ReportSucessView.as_view(), name="success"),
    path("report/", views.ReportFormView.as_view(), name="report"),
    path("denuncia/<int:pk>", views.ReportStrategy.as_view(), name="reportdetail"),
    path("noticia/<int:pk>", views.NewsStrategy.as_view(), name="newsdetail"),
    path("processo/<int:pk>", views.LawsuitStrategy.as_view(), name="lawsuitdetail"),
]
