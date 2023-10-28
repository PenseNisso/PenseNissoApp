from django.test import Client, TestCase

from company.models import Company


class SearchTestCase(TestCase):
    def setUp(self) -> None:
        Company.objects.create(name="Company 1")
        Company.objects.create(name="Company 2")
        Company.objects.create(name="Enterprise 1")
        Company.objects.create(name="Enterprise 2")
        Company.objects.create(name="Factory 1")
        Company.objects.create(name="Factory X")
        return super().setUp()

    def test_perfect_query(self) -> None:
        client = Client()
        response = client.get(path="/search/", data={"search": "Company 1"})
        self.assertSequenceEqual(
            response.context["company_list"], [Company.objects.get(name="Company 1")]
        )

    def test_narrow_query(self) -> None:
        client = Client()
        response = client.get(path="/search/", data={"search": "Enterprise"})
        self.assertEqual(response.context["company_list"].count(), 2)
        self.assertSequenceEqual(
            response.context["company_list"],
            [
                Company.objects.get(name="Enterprise 1"),
                Company.objects.get(name="Enterprise 2"),
            ],
        )

    def test_broad_query(self) -> None:
        client = Client()
        response = client.get(path="/search/", data={"search": "1"})
        self.assertEqual(response.context["company_list"].count(), 3)
        self.assertSequenceEqual(
            response.context["company_list"],
            [
                Company.objects.get(name="Company 1"),
                Company.objects.get(name="Enterprise 1"),
                Company.objects.get(name="Factory 1"),
            ],
        )

    def test_empty_query(self) -> None:
        client = Client()
        response = client.get(path="/search/", data={"search": ""})
        self.assertEqual(
            response.context["company_list"].count(), Company.objects.count()
        )

    def test_null_query(self) -> None:
        client = Client()
        response = client.get(path="/search/")
        self.assertIn("Realize uma pesquisa!", str(response.content))
