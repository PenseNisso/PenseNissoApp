from django.test import TestCase
from django.test import Client

from .models import Report, Company, ReportCategory
from .forms import ReportForm
from django.utils import timezone
from django.contrib.auth import get_user


class ReportTestCase(TestCase):
    
    def setUp(self) -> None:
        Company.objects.create(name="borin")
        ReportCategory.objects.create(name="borin",formatted_name="BORIN")
        self.current_date = timezone.now().isoformat(timespec="seconds")
        self.company = Company.objects.get(name="borin")
        self.category = ReportCategory.objects.get(name="borin")


    def test_report_request(self):
        client = Client()
        data = {"company": self.company, "category": self.category, "link": "https://borin.com", "description": "borin borin", "contact_permission": True}
        response = client.post("http://localhost:8000/info/report/", data=data)
        self.assertEqual(response.status_code, 200)

    def test_validation_company_in_form(self):
        form = ReportForm(data= {"company": "Empresa borin", "category": self.category, "link": "https://borin.com", "description": "borin borin", "contact_permission": True})
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], 'company')

    def test_validation_category_in_form(self):
        form = ReportForm(data= {"company": self.company, "category": "categoria1", "link": "https://borin.com", "description": "borin borin", "contact_permission": True})
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], 'category')

    def test_validation_link_in_form(self):
        form = ReportForm(data= {"company": self.company, "category": self.category, "link": "https://a", "description": "borin borin", "contact_permission": True})
        form.is_valid()
        self.assertEquals(list(form.errors.keys())[0], 'link')

    # def test_validation_description_in_form(self):
    #     form = ReportForm(data= {"company": self.company, "category": self.category, "link": "https://borin.com", "description": "", "contact_permission": True})
    #     form.is_valid()
    #     self.assertEquals(list(form.errors.keys())[0], 'description')


    # def test_reports_being_save(self):
    #     client = Client()
    #     data = {"company": self.company, "category": self.category, "link": "https://borin.com", "description": "borin borin", "contact_permission": True}
    #     client.post("http://localhost:8000/info/report/", data=data)

    #     report = Report.objects.all()
    #     print(report)
    #     # self.assertEquals(report.title, f"{self.current_date}-{data['company'].name}-{data['category'].name}")
