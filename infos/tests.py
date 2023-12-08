from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.utils import timezone

from company.models import Company
from user.models import User

from .forms import ReportForm
from .models import Lawsuit, News, Report, ReportCategory

factory = RequestFactory()


class ReportTestCase(TestCase):
    def setUp(self) -> None:
        Company.objects.create(name="teste")
        ReportCategory.objects.create(name="teste", formatted_name="TESTE")
        self.current_date = timezone.now().isoformat(timespec="seconds")
        self.company = Company.objects.get(name="teste")
        self.category = ReportCategory.objects.get(name="teste")

    def test_report_request(self):
        client = Client()
        data = {
            "company": self.company,
            "category": self.category,
            "link": "https://teste.com",
            "description": "teste teste",
            "contact_permission": True,
            "date": "2023-03-09",
        }
        response = client.post("/info/report/", data=data)
        self.assertEqual(response.status_code, 200)
        print("Teste Infos-Report-1: Denúncia enviada com sucesso.")

    def test_validation_company_in_form(self):
        form = ReportForm(
            data={
                "company": "Empresa teste",
                "category": self.category,
                "link": "https://teste.com",
                "description": "teste teste",
                "contact_permission": True,
                "date": "2023-03-09",
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "company")
        print("Teste Infos-Report-2: Empresa inválida negada com sucesso.")

    def test_validation_category_in_form(self):
        form = ReportForm(
            data={
                "company": self.company,
                "category": "categoria1",
                "link": "https://teste.com",
                "description": "teste teste",
                "contact_permission": True,
                "date": "2023-03-09",
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "category")
        print("Teste Infos-Report-3: Categoria inválida negada com sucesso.")

    def test_validation_link_in_form(self):
        form = ReportForm(
            data={
                "company": self.company,
                "category": self.category,
                "link": "https://a",
                "description": "teste teste",
                "contact_permission": True,
                "date": "2023-03-09",
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "link")
        print("Teste Infos-Report-4: Link inválido negado com sucesso.")

    def test_validation_description_in_form(self):
        form = ReportForm(
            data={
                "company": self.company,
                "category": self.category,
                "link": "https://teste.com",
                "description": "",
                "contact_permission": True,
                "date": "2023-03-09",
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "description")
        print("Teste Infos-Report-5: Descrição inválida negada com sucesso.")

    def test_validation_date_in_form(self):
        form = ReportForm(
            data={
                "company": self.company,
                "category": self.category,
                "link": "https://teste.com",
                "description": "teste teste",
                "contact_permission": True,
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "date")
        print("Teste Infos-Report-6: Data inválida negada com sucesso.")

    def test_report_linked_to_user(self):
        user = User.objects.create_user(username="Test User", password="testpassword")
        report = Report.objects.create(
            title="Test Report",
            content="Test Description",
            company=self.company,
            links="https://teste.com",
            user=user,
        )
        user.refresh_from_db()
        self.assertIn(report, user.reports_sent.all())
        print("Teste Infos-Report-7: Denúncia associada ao usuário com sucesso.")


class InfoDetailTestCase(TestCase):
    def setUp(self) -> None:
        self.company = Company.objects.create(name="Test Company")
        self.report = Report.objects.create(
            title="Test Report",
            content="Teste Description",
            company=self.company,
            links="https://teste.com",
        )
        self.news = News.objects.create(
            title="Test News",
            content="Test Description",
            company=self.company,
            date="2023-01-01",
            author="Myself",
        )
        self.lawsuit = Lawsuit.objects.create(
            title="Test Lawsuit",
            content="Test Description",
            company=self.company,
            source="https://teste.com",
            start_year=2023,
        )

    def test_report_details_view_status_code(self):
        response = self.client.get(reverse("infos:reportdetail", args=[self.report.id]))
        self.assertEquals(response.status_code, 200)
        print("Teste Infos-InfoDetail-1: Acesso realizado com sucesso (Cód 200).")

    def test_report_details_view_context(self):
        response = self.client.get(reverse("infos:reportdetail", args=[self.report.id]))
        self.assertEquals(response.context.get("object"), self.report)
        print(
            "Teste Infos-InfoDetail-2: Variáveis de contexto verificadas com sucesso."
        )

    def test_news_details_view_status_code(self):
        response = self.client.get(reverse("infos:newsdetail", args=[self.news.id]))
        self.assertEquals(response.status_code, 200)
        print("Teste Infos-InfoDetail-3: Acesso realizado com sucesso (Cód 200).")

    def test_news_details_view_context(self):
        response = self.client.get(reverse("infos:newsdetail", args=[self.news.id]))
        self.assertEquals(response.context.get("object"), self.news)
        print(
            "Teste Infos-InfoDetail-4: Variáveis de contexto verificadas com sucesso."
        )

    def test_lawsuit_details_view_status_code(self):
        response = self.client.get(reverse("infos:lawsuitdetail", args=[self.news.id]))
        self.assertEquals(response.status_code, 200)
        print("Teste Infos-InfoDetail-5: Acesso realizado com sucesso (Cód 200).")

    def test_lawsuit_details_view_context(self):
        response = self.client.get(reverse("infos:lawsuitdetail", args=[self.news.id]))
        self.assertEquals(response.context.get("object"), self.lawsuit)
        print(
            "Teste Infos-InfoDetail-6: Variáveis de contexto verificadas com sucesso."
        )
