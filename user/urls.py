from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    ChangePassword,
    EditProfile,
    ListaUsuarios,
    PendingReportList,
    Register,
    ReportValidation,
    UserPage,
)

app_name = "user"

urlpatterns = [
    path("", Register.as_view(), name="register"),
    path("profile/<int:pk>", UserPage.as_view(), name="profile"),
    path("usuarios/", ListaUsuarios.as_view(), name="listausuario"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path(
        "moderation/pending_reports/",
        PendingReportList.as_view(),
        name="pendingreports",
    ),
    path(
        "moderation/pending_reports/<int:pk>",
        ReportValidation.as_view(),
        name="reportvalidation",
    ),
    path(
        "profile/<int:pk>/edit/password",
        ChangePassword.as_view(),
        name="changepassword",
    ),
    path("profile/<int:pk>/edit/", EditProfile.as_view(), name="editprofile"),
]
