from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.QueryView.as_view(), name="search"),
    path("explorer", views.ExplorerView.as_view(), name="explorer"),
]
