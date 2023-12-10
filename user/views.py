from typing import Any

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import reverse
from django.views.generic import DetailView, FormView, ListView, UpdateView

from infos.models import Report

from .forms import CreateUserForm, ValidateReportForm
from .models import User


class Register(FormView):
    template_name = "register.html"
    form_class = CreateUserForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("user:login")


class UserPage(LoginRequiredMixin, DetailView):
    template_name = "profile.html"
    model = User


class ListaUsuarios(LoginRequiredMixin, ListView):
    template_name = "listausuarios.html"
    model = User


class PendingReportList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "report_list.html"
    model = Report
    permission_required = "infos.change_report"

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context["report_list"] = Report.objects.filter(status="NV")
        return context


class ReportValidation(
    LoginRequiredMixin, PermissionRequiredMixin, FormView, DetailView
):
    template_name = "report_validation.html"
    model = Report
    form_class = ValidateReportForm
    permission_required = "infos.change_report"

    def get_success_url(self) -> str:
        return reverse("user:pendingreports")

    def get_context_data(self, **kwargs: Any) -> "dict[str, Any]":
        context = super().get_context_data(**kwargs)
        context["report"].links = context.get("report").links.split("\r\n")
        return context

    def form_valid(self, form: Any) -> HttpResponse:
        data = form.cleaned_data
        report = self.get_object()
        report.gravity = data.get("gravity")
        if data.get("action") == "1":
            report.status = "AP"
        else:
            report.status = "RE"
        report.feedback = data.get("feedback")
        report.save(update_fields=["status", "gravity", "feedback"])
        return super().form_valid(form)


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "edit_profile.html"
    model = User
    fields = ["first_name", "last_name", "username", "email"]

    def test_func(self) -> bool | None:
        return self.request.get_full_path().split("/")[3] == str(self.request.user.id)

    def get_success_url(self) -> str:
        return reverse("user:profile", args=[self.request.user.id])


class ChangePassword(LoginRequiredMixin, UserPassesTestMixin, PasswordChangeView):
    template_name = "password_change.html"

    def test_func(self) -> bool | None:
        return self.request.get_full_path().split("/")[3] == str(self.request.user.id)

    def get_success_url(self) -> str:
        return reverse("user:login")
