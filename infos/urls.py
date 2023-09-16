from django.urls import path

from . import views

app_name = "infos"
urlpatterns = [
    path('confirmation/', views.ReportSucessView.as_view(), name='success'),
    path('', views.ReportFormView.as_view(), name='report'),
]