from django.test import TestCase
from django.urls import reverse

from .models import Company


# Create your tests here.
class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )

    def test_company_str(self):
        self.assertEqual(str(self.company), "Test Company")


class ExplorerViewTest(TestCase):
    def setUp(self):
        self.company1 = Company.objects.create(
            name="Test Company",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )

        self.company2 = Company.objects.create(
            name="Test Company",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )

    def test_explorer_view_status_code(self):
        response = self.client.get(reverse("company:explorer"))
        self.assertEqual(response.status_code, 200)

    def test_explorer_view_template(self):
        response = self.client.get(reverse("company:explorer"))
        self.assertTemplateUsed(response, "companies/explorer.html")

    def test_explorer_view_context(self):
        response = self.client.get(reverse("company:explorer"))
        self.assertEqual(response.context["companies"].count(), 2)


class CompanyViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )

    def test_company_view_status_code(self):
        response = self.client.get(reverse("company:company", args=[self.company.id]))
        self.assertEqual(response.status_code, 200)

    def test_company_view_template(self):
        response = self.client.get(reverse("company:company", args=[self.company.id]))
        self.assertTemplateUsed(response, "companies/company.html")

    def test_company_view_context(self):
        response = self.client.get(reverse("company:company", args=[self.company.id]))
        self.assertEqual(response.context["company"], self.company)
