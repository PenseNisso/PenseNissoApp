from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
from company.models import Company


class ComparatorViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.company1 = Company.objects.create(
            name="Company 1",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )
        self.company2 = Company.objects.create(
            name="Company 2",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )
        self.company3 = Company.objects.create(
            name="Company 3",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )

    def test_get_method(self):
        response = self.client.get(reverse("comparator:comparator"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "comparator.html")
        print("Teste Comparator-View-1: Acesso realizado com sucesso (Cód 200).")

    def test_post_method_add_company(self):
        response = self.client.post(
            reverse("comparator:comparator"), {"company": "Company 2"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Company 2", self.client.session["selected_companies"])
        print("Teste Comparator-View-2: Empresa adicionada com sucesso.")


class DeleteViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.company1 = Company.objects.create(
            name="Company 1",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )
        self.company2 = Company.objects.create(
            name="Company 2",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )

    def test_delete_view(self):
        response = self.client.post(
            reverse("comparator:comparator"), {"company": "Company 1"}
        )
        response = self.client.get(
            reverse("comparator:delete"), {"company": "Company 1"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("Company 1", self.client.session["selected_companies"])
        print("Teste Comparator-DeleteView-1: Empresa deletada com sucesso.")
