from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from infos.models import Lawsuit, News, Report, ReportCategory

from .models import Company


class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )
        self.report = Report.objects.create(
            title="Test Report 1",
            content="Teste Description 1",
            company=self.company,
            links="https://teste.com",
            status="AP",
            gravity="1",
            date=now() - timedelta(days=15),
        )

    def test_company_str(self):
        self.assertEqual(str(self.company), "Test Company")
        print("Teste Company-Model-1: Objeto criado com sucesso.")

    def test_company_score(self):
        self.assertEquals(self.company.compute_score(), 4.08)
        print("Teste Company-Model-2: Score calculado com sucesso")

    def test_update_company_score(self):
        Report.objects.create(
            title="Test Report 2",
            content="Teste Description 2",
            company=self.company,
            links="https://teste.com",
            status="AP",
            gravity="4",
            date=now() - timedelta(days=1200),
        )
        self.assertEquals(self.company.compute_score(), 3.89)
        print("Teste Company-Model-3: Score atualizado com sucesso")


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
        print("Teste Company-View-1: Acesso realizado com sucesso (Cód 200).")

    def test_company_view_template(self):
        response = self.client.get(reverse("company:company", args=[self.company.id]))
        self.assertTemplateUsed(response, "companies/company.html")
        print("Teste Company-View-2: Template aplicado com sucesso.")

    def test_company_view_context(self):
        response = self.client.get(reverse("company:company", args=[self.company.id]))
        self.assertEqual(response.context["company"], self.company)
        print("Teste Company-View-3: Variáveis de contexto verificadas com sucesso.")


class InfoListTest(TestCase):
    def setUp(self) -> None:
        self.company = Company.objects.create(
            name="Test Company",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )
        Report.objects.create(
            title="Test Report 1",
            content="Teste Description 1",
            company=self.company,
            links="https://teste.com",
            status="AP",
        )
        Report.objects.create(
            title="Test Report 2",
            content="Teste Description 2",
            company=self.company,
            links="https://teste.com",
            status="AP",
        )
        News.objects.create(
            title="Test News 1",
            content="Test Description 1",
            company=self.company,
            date="2023-01-01",
            author="myself",
        )
        News.objects.create(
            title="Test News 2",
            content="Test Description 2",
            company=self.company,
            date="2023-01-01",
            author="myself",
        )
        Lawsuit.objects.create(
            title="Test Lawsuit 1",
            content="Test Description 1",
            company=self.company,
            source="https://teste.com",
            start_year=2023,
        )
        Lawsuit.objects.create(
            title="Test Lawsuit 2",
            content="Test Description 2",
            company=self.company,
            source="https://teste.com",
            start_year=2022,
            resolution_year=2023,
        )

    def test_full_report_list(self):
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertSequenceEqual(
            response.context.get("infos"), list(Report.objects.all())
        )
        print("Teste Company-InfoList-1: Denúncias obtidas com sucesso.")

    def test_filtered_report_list(self):
        report = Report.objects.create(
            title="Test Report 3",
            content="Teste Description 3",
            company=Company.objects.create(name="Other Company"),
            links="https://teste.com",
            status="AP",
        )
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertNotIn(report, response.context.get("infos"))
        print("Teste Company-InfoList-2: Denúncias filtradas com sucesso.")

    def test_new_report_in_list(self):
        report = Report.objects.create(
            title="Test Report 3",
            content="Teste Description 3",
            company=self.company,
            links="https://teste.com",
            status="AP",
        )
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertIn(report, response.context.get("infos"))
        print("Teste Company-InfoList-3: Denúncias atualizadas com sucesso.")

    def test_only_approved_reports_in_list(self):
        report1 = Report.objects.create(
            title="Test Report 3",
            content="Teste Description 3",
            company=self.company,
            links="https://teste.com",
            status="NV",
        )
        report2 = Report.objects.create(
            title="Test Report 4",
            content="Teste Description 4",
            company=self.company,
            links="https://teste.com",
            status="RE",
        )
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertNotIn(report1, response.context.get("infos"))
        self.assertNotIn(report2, response.context.get("infos"))
        print("Teste Company-InfoList-4: Denúncias filtradas com sucesso.")

    def test_full_news_list(self):
        response = self.client.get(reverse("company:news", args=[self.company.id]))
        self.assertSequenceEqual(
            response.context.get("infos"), list(News.objects.all())
        )
        print("Teste Company-InfoList-5: Notícias obtidas com sucesso.")

    def test_filtered_news_list(self):
        news = News.objects.create(
            title="Test News 3",
            content="Test Description 3",
            company=Company.objects.create(name="Other Company"),
            date="2023-01-01",
            author="myself",
        )
        response = self.client.get(reverse("company:news", args=[self.company.id]))
        self.assertNotIn(news, response.context.get("infos"))
        print("Teste Company-InfoList-6: Notícias obtidas com sucesso.")

    def test_new_news_in_list(self):
        news = News.objects.create(
            title="Test News 3",
            content="Test Description 3",
            company=self.company,
            date="2023-01-01",
            author="myself",
        )
        response = self.client.get(reverse("company:news", args=[self.company.id]))
        self.assertIn(news, response.context.get("infos"))
        print("Teste Company-InfoList-7: Notícias atualizadas com sucesso.")

    def test_full_lawsuit_list(self):
        response = self.client.get(reverse("company:lawsuits", args=[self.company.id]))
        self.assertSequenceEqual(
            response.context.get("infos"), list(Lawsuit.objects.all())
        )
        print("Teste Company-InfoList-8: Processos obtidos com sucesso.")

    def test_filtered_lawsuit_list(self):
        lawsuit = Lawsuit.objects.create(
            title="Test Lawsuit 3",
            content="Test Description 3",
            company=Company.objects.create(name="Other Company"),
            source="https://teste.com",
            start_year=2023,
        )
        response = self.client.get(reverse("company:lawsuits", args=[self.company.id]))
        self.assertNotIn(lawsuit, response.context.get("infos"))
        print("Teste Company-InfoList-9: Processos obtidos com sucesso.")

    def test_new_lawsuit_in_list(self):
        lawsuit = Lawsuit.objects.create(
            title="Test Lawsuit 3",
            content="Test Description 3",
            company=self.company,
            source="https://source.com",
            start_year=2023,
        )
        response = self.client.get(reverse("company:lawsuits", args=[self.company.id]))
        self.assertIn(lawsuit, response.context.get("infos"))
        print("Teste Company-InfoList-10: Processos atualizados com sucesso.")
