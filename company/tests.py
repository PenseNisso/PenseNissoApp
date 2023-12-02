from django.test import TestCase
from django.urls import reverse

from infos.models import Lawsuit, News, Report, ReportCategory

from .models import Company


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
        )
        Report.objects.create(
            title="Test Report 2",
            content="Teste Description 2",
            company=self.company,
            links="https://teste.com",
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

    def test_filtered_report_list(self):
        report = Report.objects.create(
            title="Test Report 3",
            content="Teste Description 3",
            company=Company.objects.create(name="Other Company"),
            links="https://teste.com",
        )
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertNotIn(report, response.context.get("infos"))

    def test_new_report_in_list(self):
        report = Report.objects.create(
            title="Test Report 3",
            content="Teste Description 3",
            company=self.company,
            links="https://teste.com",
        )
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertIn(report, response.context.get("infos"))

    def test_full_news_list(self):
        response = self.client.get(reverse("company:news", args=[self.company.id]))
        self.assertSequenceEqual(
            response.context.get("infos"), list(News.objects.all())
        )

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

    def test_full_lawsuit_list(self):
        response = self.client.get(reverse("company:lawsuits", args=[self.company.id]))
        self.assertSequenceEqual(
            response.context.get("infos"), list(Lawsuit.objects.all())
        )

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
