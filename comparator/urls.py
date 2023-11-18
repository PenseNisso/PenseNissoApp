from django.urls import path

from . import views

app_name = "comparator"
urlpatterns = [
    path("", views.ComparatorView.as_view(), name="comparator"),
]
