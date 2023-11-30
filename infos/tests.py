from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.utils import timezone

from company.models import Company

from .forms import ReportForm
from .models import Report, ReportCategory

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
        }
        response = client.post("/info/report/", data=data)
        self.assertEqual(response.status_code, 200)

    def test_validation_company_in_form(self):
        form = ReportForm(
            data={
                "company": "Empresa teste",
                "category": self.category,
                "link": "https://teste.com",
                "description": "teste teste",
                "contact_permission": True,
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "company")

    def test_validation_category_in_form(self):
        form = ReportForm(
            data={
                "company": self.company,
                "category": "categoria1",
                "link": "https://teste.com",
                "description": "teste teste",
                "contact_permission": True,
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "category")

    def test_validation_link_in_form(self):
        form = ReportForm(
            data={
                "company": self.company,
                "category": self.category,
                "link": "https://a",
                "description": "teste teste",
                "contact_permission": True,
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "link")

    def test_validation_description_in_form(self):
        form = ReportForm(
            data={
                "company": self.company,
                "category": self.category,
                "link": "https://teste.com",
                "description": "",
                "contact_permission": True,
            }
        )
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], "description")


class InfoDetailTestCase(TestCase):
    def setUp(self) -> None:
        self.company = Company.objects.create(name="Test Company")
        self.report = Report.objects.create(
            title="Test Report",
            content="Teste Description",
            company=self.company,
            links="https://teste.com",
        )

    def test_report_details_view_status_code(self):
        response = self.client.get(reverse("infos:reportdetail", args=[self.report.id]))
        self.assertEquals(response.status_code, 200)
    
    def test_report_details_view_context(self):
        response = self.client.get(reverse("infos:reportdetail", args=[self.report.id]))
        self.assertEquals(response.context.get("object"), self.report)
