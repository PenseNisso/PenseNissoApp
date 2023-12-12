from typing import Any

from django.views.generic import TemplateView

from infos.models import News


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context.update({"recent_news": News.objects.all().order_by("-date")[:5]})
        return context
