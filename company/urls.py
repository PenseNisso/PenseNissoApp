from django.urls import path

from . import views

app_name = "company"
urlpatterns = [
    path('', views.explorer, name='explorer'),
    #path('explorador/', views.explorer, name='explorer'),
    path('<int:company_id>/', views.company, name='company'),
    path('<int:company_id>/noticias/',views.news, name="news"),
    path('<int:company_id>/processos/',views.lawsuits, name="lawsuits"),
    path('<int:company_id>/denuncias/',views.reports, name="reports"),
]
