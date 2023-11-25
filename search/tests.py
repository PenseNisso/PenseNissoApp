from django.test import Client, TestCase

from company.models import Company

from .views import SearchView


class TrigramTestCase(TestCase):
    def setUp(self) -> None:
        self.strings = ["abcdefghijklmnopqrstuvwxyz", "powder", "bee", "cream"]
        self.trigram = SearchView(2)
        self.trigram_score_three = SearchView(3)

        return super().setUp()

    def test_basic_match(self) -> None:
        result = self.trigram.filter_set(keyword="powd", set=self.strings)
        self.assertListEqual(result, ["powder"])

    def test_basic_match_multiple(self) -> None:
        result = self.trigram.filter_set(keyword="powd crea", set=self.strings)
        self.assertListEqual(result, ["powder", "cream"])

    def test_basic_match_none(self) -> None:
        result = self.trigram.filter_set(keyword="pow", set=self.strings)
        self.assertListEqual(result, [])

    def test_score_test(self) -> None:
        result_three_score = self.trigram_score_three.filter_set(
            keyword="pow", set=self.strings
        )
        self.assertListEqual(result_three_score, [])


class SearchTestCase(TestCase):
    def setUp(self) -> None:
        Company.objects.create(name="Company 1")
        Company.objects.create(name="Company 2")
        Company.objects.create(name="Enterprise 1")
        Company.objects.create(name="Enterprise 2")
        Company.objects.create(name="Factory 1")
        Company.objects.create(name="Factory X")
        client = Client()
        return super().setUp()

    def test_perfect_query(self) -> None:
        response = self.client.get(path="/search/", data={"search": "Company 1"})
        self.assertSequenceEqual(
            response.context["company_list"],
            [
                Company.objects.get(name="Company 1"),
                Company.objects.get(name="Company 2"),
            ],
        )

    def test_narrow_query(self) -> None:
        response = self.client.get(path="/search/", data={"search": "Enterprise"})
        self.assertEqual(response.context["company_list"].count(), 2)
        self.assertSequenceEqual(
            response.context["company_list"],
            [
                Company.objects.get(name="Enterprise 1"),
                Company.objects.get(name="Enterprise 2"),
            ],
        )

    def test_broad_query(self) -> None:
        response = self.client.get(path="/search/", data={"search": "1"})
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
        response = self.client.get(path="/search/", data={"search": ""})
        self.assertEqual(
            response.context["company_list"].count(), Company.objects.count()
        )

    def test_null_query(self) -> None:
        response = self.client.get(path="/search/")
        self.assertIn("Realize uma pesquisa!", str(response.content))

    def test_spelling_mistake(self) -> None:
        response = self.client.get(path="/search/", data={"search": "compani"})
        self.assertSequenceEqual(
            response.context["company_list"],
            [
                Company.objects.get(name="Company 1"),
                Company.objects.get(name="Company 2"),
            ],
        )

    def test_gibberish(self) -> None:
        response = self.client.get(path="/search/", data={"search": "coamptrajsy"})
        self.assertSequenceEqual(
            response.context["company_list"],
            [],
        )
