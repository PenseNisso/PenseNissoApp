from django.urls import path

from . import views

app_name = "infos"
urlpatterns = [
    path('', views.explorer, name='explorer'),
    #path('explorador/', views.explorer, name='explorer'),
    path('<int:company_id>/', views.company, name='company'),
]
