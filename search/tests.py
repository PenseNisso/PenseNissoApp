from django.test import Client, TestCase

from company.models import Company

from .views import ExplorerView, QueryView, SearchView


class TrigramTestCase(TestCase):
    def setUp(self) -> None:
        self.strings = ["abcdefghijklmnopqrstuvwxyz", "powder", "bee", "cream"]
        self.trigram = QueryView(2)
        self.trigram_score_three = QueryView(3)

        return super().setUp()

    def test_basic_match(self) -> None:
        result = self.trigram.filter_set(keyword="powd", set=self.strings)
        self.assertListEqual(result, ["powder"])
        print(
            "Teste Search-Trigram-1: Busca retornou resultado esperado (podw -> powder)."
        )

    def test_basic_match_multiple(self) -> None:
        result = self.trigram.filter_set(keyword="powd crea", set=self.strings)
        self.assertListEqual(result, ["powder", "cream"])
        print(
            "Teste Search-Trigram-2: Busca retornou resultado esperado (podw crea -> powder, cream)."
        )

    def test_basic_match_none(self) -> None:
        result = self.trigram.filter_set(keyword="pow", set=self.strings)
        self.assertListEqual(result, [])
        print("Teste Search-Trigram-3: Busca retornou resultado esperado (pow -> []).")

    def test_score_test(self) -> None:
        result_three_score = self.trigram_score_three.filter_set(
            keyword="powd", set=self.strings
        )
        self.assertListEqual(result_three_score, [])
        print("Teste Search-Trigram-4: Busca retornou resultado esperado (powd -> []).")


class SearchTestCase(TestCase):
    def setUp(self) -> None:
        Company.objects.create(name="Company 1")
        Company.objects.create(name="Company 2")
        Company.objects.create(name="Enterprise 1")
        Company.objects.create(name="Enterprise 2")
        Company.objects.create(name="Factory 1")
        Company.objects.create(name="Factory X")
        self.client = Client()
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
        print(
            "Teste Search-Query-1: Busca retornou resultados esperados (Company 1 -> Company 1, Company 2)."
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
        print(
            "Teste Search-Query-2: Busca retornou resultados esperados (Enterprise -> Enterprise 1, Enterprise 2)."
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
        print(
            "Teste Search-Query-3: Busca retornou resultados esperados (1 -> Company 1, Enterprise 1, Factory 1)."
        )

    def test_empty_query(self) -> None:
        response = self.client.get(path="/search/", data={"search": ""})
        self.assertEqual(
            response.context["company_list"].count(), Company.objects.count()
        )
        print("Teste Search-Query-4: Busca retornou todos os objetos.")

    def test_null_query(self) -> None:
        response = self.client.get(path="/search/")
        self.assertIn("Realize uma pesquisa!", str(response.content))
        print("Teste Search-Query-5: Busca retornou mensagem de erro.")

    def test_spelling_mistake(self) -> None:
        response = self.client.get(path="/search/", data={"search": "compani"})
        self.assertSequenceEqual(
            response.context["company_list"],
            [
                Company.objects.get(name="Company 1"),
                Company.objects.get(name="Company 2"),
            ],
        )
        print(
            "Teste Search-Query-6: Busca retornou resultados esperados (compani -> Company 1, Company 2)."
        )

    def test_gibberish(self) -> None:
        response = self.client.get(path="/search/", data={"search": "coamptrajsy"})
        self.assertSequenceEqual(
            response.context["company_list"],
            [],
        )
        print(
            "Teste Search-Query-7: Busca retornou resultados esperados (coamptrajsy -> [])."
        )


class ExplorerTestCase(TestCase):
    def setUp(self) -> None:
        Company.objects.create(name="Company 1")
        Company.objects.create(name="Company 2")
        Company.objects.create(name="Enterprise 1")
        Company.objects.create(name="Enterprise 2")
        Company.objects.create(name="Factory 1")
        Company.objects.create(name="Factory X")
        self.companies = list(Company.objects.all())
        self.client = Client()
        return super().setUp()

    def test_view_status_code(self) -> None:
        response = self.client.get(path="/search/explorer")
        self.assertEqual(response.status_code, 200)
        print("Teste Search-Explorer-1: Acesso realizado com sucesso (Cód 200).")

    def test_view_template(self) -> None:
        response = self.client.get(path="/search/explorer")
        self.assertTemplateUsed(response, "explorer.html")
        print("Teste Search-Explorer-2: Template aplicado com sucesso.")

    def test_view_context(self) -> None:
        response = self.client.get(path="/search/explorer")
        self.assertEqual(response.context["company_list"].count(), 6)
        self.assertSequenceEqual(response.context["company_list"], self.companies)
        print(
            "Teste Search-Explorer-3: Explorador contém variáveis de contexto corretas."
        )

    def test_explorer_update(self) -> None:
        response = self.client.get(path="/search/explorer")
        self.assertEqual(response.context["company_list"].count(), 6)
        self.companies.append(Company.objects.create(name="Factory T"))
        response = self.client.get(path="/search/explorer")
        self.assertEqual(response.context["company_list"].count(), 7)
        self.assertSequenceEqual(response.context["company_list"], self.companies)
        print("Teste Search-Explorer-4: Explorador atualizado com sucesso.")
