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


class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_User", password="testpassword"
        )

    def test_profile_view_status_code(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_template(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertTemplateUsed(response, "profile.html")

    def test_profile_view_context(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertEqual(response.context["object"].username, "Test_User")


class RegisterViewTest(TestCase):
    def test_register_view_status_code(self):
        response = self.client.get(reverse("user:register"))
        self.assertEqual(response.status_code, 200)

    def test_register_view_template(self):
        response = self.client.get(reverse("user:register"))
        self.assertTemplateUsed(response, "register.html")


class LoginViewTest(TestCase):
    def test_login_view_status_code(self):
        response = self.client.get(reverse("user:login"))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        response = self.client.get(reverse("user:login"))
        self.assertTemplateUsed(response, "login.html")


class LogoutViewTest(TestCase):
    def test_logout_view_status_code(self):
        response = self.client.get(reverse("user:logout"))
        self.assertEqual(response.status_code, 200)

    def test_logout_view_template(self):
        response = self.client.get(reverse("user:logout"))
        self.assertTemplateUsed(response, "logout.html")
