from typing import Any
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context["images"] = ["images/cap1.jpg", "images/cap2.jpg", "images/cap3.jpg"]
        return context