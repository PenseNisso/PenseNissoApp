from django.contrib.auth import views as auth_view
from django.urls import path

from .views import Cadastro, ListaUsuarios, PaginaUsuario

app_name = "app_usuario"

urlpatterns = [
    path("", Cadastro.as_view(), name="cadastro"),
    path("perfil/<int:pk>", PaginaUsuario.as_view(), name="perfilusuario"),
    path("usuarios/", ListaUsuarios.as_view(), name="listausuario"),
    path(
        "login/", auth_view.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
]
