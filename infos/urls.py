from django.urls import path

from . import views

app_name = "infos"
urlpatterns = [
    path('report/confirmation', views.ReportSucessView, name='success'),
    path('report/', views.ReportFormView, name='report'),
]