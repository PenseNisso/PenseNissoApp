from django.test import TestCase
from django.urls import reverse

from .models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_User", password="testpassword"
        )

    def test_user_str(self):
        self.assertEqual(str(self.user), "Test_User")
        print("Teste User-Model-1: Usuário criado com sucesso.")


class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_User", password="testpassword"
        )

    def test_profile_view_status_code(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        print("Teste User-ProfileView-1: Login realizado com sucesso (Cód 200).")

    def test_profile_view_template(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertTemplateUsed(response, "profile.html")
        print("Teste User-ProfileView-2: Template aplicado com sucesso.")

    def test_profile_view_context(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertEqual(response.context["object"].username, "Test_User")
        print(
            "Teste User-ProfileView-3: Variáveis de contexto verificadas com sucesso."
        )


class RegisterViewTest(TestCase):
    def test_register_view_status_code(self):
        response = self.client.get(reverse("user:register"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-RegisterView-1: Acesso realizado com sucesso (Cód 200).")

    def test_register_view_template(self):
        response = self.client.get(reverse("user:register"))
        self.assertTemplateUsed(response, "register.html")
        print("Teste User-RegisterView-2: Template usado com sucesso.")


class LoginViewTest(TestCase):
    def test_login_view_status_code(self):
        response = self.client.get(reverse("user:login"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-LoginView-1: Acesso realizado com sucesso (Cód 200).")

    def test_login_view_template(self):
        response = self.client.get(reverse("user:login"))
        self.assertTemplateUsed(response, "login.html")
        print("Teste User-LoginView-2: Template usado com sucesso.")


class LogoutViewTest(TestCase):
    def test_logout_view_status_code(self):
        response = self.client.get(reverse("user:logout"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-LogoutView-1: Acesso realizado com sucesso (Cód 200).")

    def test_logout_view_template(self):
        response = self.client.get(reverse("user:logout"))
        self.assertTemplateUsed(response, "logout.html")
        print("Teste User-LoginView-2: Template usado com sucesso.")
