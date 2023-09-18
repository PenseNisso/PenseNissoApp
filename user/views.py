from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import DetailView, FormView, ListView

from .forms import CreateUserForm
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
