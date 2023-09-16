from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.views.generic import DetailView, FormView, ListView

from .forms import CriarContaForm
from .models import Usuario


# Create your views here.
class Cadastro(FormView):
    template_name = "cadastro.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_usuario:login')


class PaginaUsuario(LoginRequiredMixin, DetailView):
    template_name = "perfilusuario.html"
    model = Usuario


class ListaUsuarios(LoginRequiredMixin, ListView):
    template_name = "listausuarios.html"
    model = Usuario


# def usuarios(request):
#     # guardando os dados fornecidos no bd
#     novo_usuario = Usuario()
#     novo_usuario.nome = request.POST.get('nome')
#     novo_usuario.e_mail = request.POST.get('e_mail')
#     novo_usuario.senha = request.POST.get('senha')
#     novo_usuario.save()
#     # exibindo os usuarios
#     usuarios = {
#         'usuarios': Usuario.objects.all()
#     }
#     # direciona os dados para a pagina com a lista
#     return render(request, 'usuarios.html', usuarios)
