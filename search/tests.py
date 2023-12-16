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
        Company.objects.create(
            name="Company 1", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Company 2", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Enterprise 1", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Enterprise 2", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Factory 1", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Factory X", logo="company/logo/23/12/10/test_logo.png"
        )
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
        self.assertIn("Realize uma pesquisa!", str(response.content))
        print("Teste Search-Query-4: Busca retornou todos os objetos.")

    def test_null_query(self) -> None:
        self.client.session.flush()
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
        response = self.client.get(path="/search/", data={"search": "entemansmdnasd"})
        self.assertSequenceEqual(
            response.context["company_list"],
            [],
        )
        print(
            "Teste Search-Query-7: Busca retornou resultados esperados (entemansmdnasd -> [])."
        )


class ExplorerTestCase(TestCase):
    def setUp(self) -> None:
        self.company_1 = Company.objects.create(
            name="Company 1", logo="company/logo/23/12/10/test_logo.png"
        )
        self.company_2 = Company.objects.create(
            name="Company 2", logo="company/logo/23/12/10/test_logo.png"
        )
        self.enterprise_1 = Company.objects.create(
            name="Enterprise 1", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Enterprise 2", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Factory 1", logo="company/logo/23/12/10/test_logo.png"
        )
        Company.objects.create(
            name="Factory X", logo="company/logo/23/12/10/test_logo.png"
        )
        self.company_1.reports.create(
            title="Report1",
            content="",
            links="a.com",
            date="2023-01-01",
            gravity="4",
            status="AP",
        )
        self.company_2.news.create(
            title="News1", content="", date="2023-01-01", author="M"
        )
        self.enterprise_1.lawsuits.create(
            title="Lawsuit1", content="", source="a.com", start_year=2000
        )
        self.companies = list(Company.objects.all().order_by("name"))
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
        self.companies.append(
            Company.objects.create(
                name="Factory T", logo="company/logo/23/12/10/test_logo.png"
            )
        )
        self.companies.sort(key=lambda company: company.name)
        response = self.client.get(path="/search/explorer")
        self.assertEqual(response.context["company_list"].count(), 7)
        self.assertSequenceEqual(response.context["company_list"], self.companies)
        print("Teste Search-Explorer-4: Explorador atualizado com sucesso.")

    def test_explorer_filter_report(self) -> None:
        response = self.client.get(path="/search/explorer", data={"has_reports": "yes"})
        self.assertEqual(response.context["company_list"].count(), 1)
        self.assertSequenceEqual(response.context["company_list"], [self.company_1])
        response = self.client.get(path="/search/explorer", data={"has_reports": "no"})
        self.assertEqual(response.context["company_list"].count(), 5)
        self.assertSequenceEqual(
            response.context["company_list"],
            [c for c in self.companies if c != self.company_1],
        )
        print("Teste Search-Explorer-5: Filtro aplicado com sucesso.")

    def test_explorer_filter_news(self) -> None:
        response = self.client.get(path="/search/explorer", data={"has_news": "yes"})
        self.assertEqual(response.context["company_list"].count(), 1)
        self.assertSequenceEqual(response.context["company_list"], [self.company_2])
        response = self.client.get(path="/search/explorer", data={"has_news": "no"})
        self.assertEqual(response.context["company_list"].count(), 5)
        self.assertSequenceEqual(
            response.context["company_list"],
            [c for c in self.companies if c != self.company_2],
        )
        print("Teste Search-Explorer-6: Filtro aplicado com sucesso.")

    def test_explorer_filter_lawsuit(self) -> None:
        response = self.client.get(
            path="/search/explorer", data={"has_lawsuits": "yes"}
        )
        self.assertEqual(response.context["company_list"].count(), 1)
        self.assertSequenceEqual(response.context["company_list"], [self.enterprise_1])
        response = self.client.get(path="/search/explorer", data={"has_lawsuits": "no"})
        self.assertEqual(response.context["company_list"].count(), 5)
        self.assertSequenceEqual(
            response.context["company_list"],
            [c for c in self.companies if c != self.enterprise_1],
        )
        print("Teste Search-Explorer-7: Filtro aplicado com sucesso.")

    def test_explorer_sorting_default(self) -> None:
        response = self.client.get(path="/search/explorer")
        company_list = list(response.context["company_list"])
        self.assertTrue(
            all(
                company_list[i].name <= company_list[i + 1].name
                for i in range(len(company_list) - 1)
            )
        )
        print("Teste Search-Explorer-8: Ordenação aplicada com sucesso.")

    def test_explorer_sorting_alphabetical_descending(self) -> None:
        response = self.client.get(
            path="/search/explorer", data={"sorting": "alphabetical_descending"}
        )
        company_list = list(response.context["company_list"])
        self.assertTrue(
            all(
                company_list[i].name >= company_list[i + 1].name
                for i in range(len(company_list) - 1)
            )
        )
        print("Teste Search-Explorer-9: Ordenação aplicada com sucesso.")

    def test_explorer_sorting_most_reports(self) -> None:
        response = self.client.get(
            path="/search/explorer", data={"sorting": "most_reports"}
        )
        company_list = list(response.context["company_list"])
        self.assertTrue(
            all(
                company_list[i].reports.count() >= company_list[i + 1].reports.count()
                for i in range(len(company_list) - 1)
            )
        )
        print("Teste Search-Explorer-10: Ordenação aplicada com sucesso.")

    def test_explorer_sorting_least_reports(self) -> None:
        response = self.client.get(
            path="/search/explorer", data={"sorting": "least_reports"}
        )
        company_list = list(response.context["company_list"])
        self.assertTrue(
            all(
                company_list[i].reports.count() <= company_list[i + 1].reports.count()
                for i in range(len(company_list) - 1)
            )
        )
        print("Teste Search-Explorer-11: Ordenação aplicada com sucesso.")

    def test_explorer_sorting_highest_score(self) -> None:
        response = self.client.get(
            path="/search/explorer", data={"sorting": "highest_score"}
        )
        company_list = list(response.context["company_list"])
        self.assertTrue(
            all(
                company_list[i].compute_score() >= company_list[i + 1].compute_score()
                for i in range(len(company_list) - 1)
            )
        )
        print("Teste Search-Explorer-12: Ordenação aplicada com sucesso.")

    def test_explorer_sorting_lowest_score(self) -> None:
        response = self.client.get(
            path="/search/explorer", data={"sorting": "lowest_score"}
        )
        company_list = list(response.context["company_list"])
        self.assertTrue(
            all(
                company_list[i].compute_score() <= company_list[i + 1].compute_score()
                for i in range(len(company_list) - 1)
            )
        )

        print("Teste Search-Explorer-13: Ordenação aplicada com sucesso.")
