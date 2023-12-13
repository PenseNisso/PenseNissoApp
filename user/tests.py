from django.contrib.auth.models import Permission
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from company.models import Company, CompanySuggestionModel
from infos.models import Report

from .forms import ValidateReportForm, ValidateSuggestionForm
from .models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_User", password="testpassword"
        )

    def test_user_str(self):
        self.assertEqual(str(self.user), "Test_User")
        print("Teste User-Model-1: Usuário criado com sucesso.")


class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_User", password="testpassword"
        )

    def test_profile_view_status_code(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        print("Teste User-ProfileView-1: Login realizado com sucesso (Cód 200).")

    def test_profile_view_template(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertTemplateUsed(response, "profile.html")
        print("Teste User-ProfileView-2: Template aplicado com sucesso.")

    def test_profile_view_context(self):
        self.client.login(username="Test_User", password="testpassword")
        response = self.client.get(reverse("user:profile", args=[self.user.id]))
        self.assertEqual(response.context["object"].username, "Test_User")
        print(
            "Teste User-ProfileView-3: Variáveis de contexto verificadas com sucesso."
        )


class RegisterViewTest(TestCase):
    def test_register_view_status_code(self):
        response = self.client.get(reverse("user:register"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-RegisterView-1: Acesso realizado com sucesso (Cód 200).")

    def test_register_view_template(self):
        response = self.client.get(reverse("user:register"))
        self.assertTemplateUsed(response, "register.html")
        print("Teste User-RegisterView-2: Template usado com sucesso.")


class LoginViewTest(TestCase):
    def test_login_view_status_code(self):
        response = self.client.get(reverse("user:login"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-LoginView-1: Acesso realizado com sucesso (Cód 200).")

    def test_login_view_template(self):
        response = self.client.get(reverse("user:login"))
        self.assertTemplateUsed(response, "login.html")
        print("Teste User-LoginView-2: Template usado com sucesso.")


class LogoutViewTest(TestCase):
    def test_logout_view_status_code(self):
        response = self.client.get(reverse("user:logout"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-LogoutView-1: Acesso realizado com sucesso (Cód 200).")

    def test_logout_view_template(self):
        response = self.client.get(reverse("user:logout"))
        self.assertTemplateUsed(response, "logout.html")
        print("Teste User-LoginView-2: Template usado com sucesso.")


class ReportValidationTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="Test User", password="userpassword"
        )
        self.moderator = User.objects.create_user(
            username="Test Moderator", password="moderatorpassword"
        )
        self.moderator.user_permissions.add(
            Permission.objects.get(codename="change_report")
        )
        self.company = Company.objects.create(
            name="Test Company",
            description="Test Description",
            logo="company/logo/21/09/16/test_logo.png",
        )
        self.report = Report.objects.create(
            title="Test Report",
            content="Teste Description",
            company=self.company,
            links="https://teste.com",
            status="NV",
        )

    def test_pending_view_status_code(self):
        self.client.login(username="Test User", password="userpassword")
        response = self.client.get(reverse("user:pendingreports"))
        self.assertEqual(response.status_code, 403)
        self.client.login(username="Test Moderator", password="moderatorpassword")
        response = self.client.get(reverse("user:pendingreports"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-ReportValidation-1: Acesso restringido com sucesso.")

    def test_validation_view_status_code(self):
        self.client.login(username="Test User", password="userpassword")
        response = self.client.get(
            reverse("user:reportvalidation", args=[self.report.id])
        )
        self.assertEquals(response.status_code, 403)
        self.client.login(username="Test Moderator", password="moderatorpassword")
        response = self.client.get(
            reverse("user:reportvalidation", args=[self.report.id])
        )
        self.assertEquals(response.status_code, 200)
        print("Teste User-ReportValidation-2: Acesso restringido com sucesso.")

    def test_pending_view_context(self):
        Report.objects.create(
            title="Test Report 2",
            content="Teste Description",
            company=self.company,
            links="https://teste.com",
            status="AP",
        )
        Report.objects.create(
            title="Test Report 3",
            content="Teste Description",
            company=self.company,
            links="https://teste.com",
            status="RE",
        )
        self.client.login(username="Test Moderator", password="moderatorpassword")
        response = self.client.get(reverse("user:pendingreports"))
        self.assertSequenceEqual(response.context.get("report_list"), [self.report])
        print(
            "Teste User-ReportValidation-3: Variáveis de contexto verificadas com sucesso."
        )

    def test_validation_report_valid(self):
        form = ValidateReportForm(data={"action": "1", "gravity": "1", "feedback": "."})
        form.is_valid()
        self.assertDictEqual(form.errors, {})
        print("Teste User-ReportValidation-4: Feedback enviado com sucesso.")

    def test_validation_action_in_form(self):
        form = ValidateReportForm(data={"gravity": "1", "feedback": "."})
        form.is_valid()
        self.assertIn("action", form.errors)
        print("Teste User-ReportValidation-5: Ação inválida negada com sucesso.")

    def test_validation_gravity_in_form(self):
        form = ValidateReportForm(data={"action": "1", "feedback": "."})
        form.is_valid()
        self.assertIn("gravity", form.errors)
        print("Teste User-ReportValidation-6: Gravidade inválida negada com sucesso.")

    def test_validation_feedback_in_form(self):
        form = ValidateReportForm(data={"action": "1", "gravity": "1"})
        form.is_valid()
        self.assertIn("feedback", form.errors)
        print("Teste User-ReportValidation-6: Feedback inválido negada com sucesso.")

    def test_can_approve_report(self):
        self.client.login(username="Test Moderator", password="moderatorpassword")
        self.client.post(
            reverse("user:reportvalidation", args=[self.report.id]),
            data={"action": "1", "gravity": "1", "feedback": "."},
        )
        # check if the report's status was changed successfully
        self.report.refresh_from_db()
        self.assertEquals(self.report.status, "AP")
        # check if the report is no longer on pending reports list
        response = self.client.get(reverse("user:pendingreports"))
        self.assertNotIn(self.report, response.context.get("report_list"))
        # check if the report appears on company's report list
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertIn(
            self.report,
            response.context.get("infos"),
        )
        print("Teste User-ReportValidation-8: Denúncia aprovada com sucesso.")

    def test_can_deny_report(self):
        self.client.login(username="Test Moderator", password="moderatorpassword")
        self.client.post(
            reverse("user:reportvalidation", args=[self.report.id]),
            data={"action": "0", "gravity": "1", "feedback": "."},
        )
        # check if the report's status was changed successfully
        self.report.refresh_from_db()
        self.assertEquals(self.report.status, "RE")
        # check if the report is no longer on pending reports list
        response = self.client.get(reverse("user:pendingreports"))
        self.assertNotIn(self.report, response.context.get("report_list"))
        # check if the report appears on company's report list
        response = self.client.get(reverse("company:reports", args=[self.company.id]))
        self.assertNotIn(
            self.report,
            response.context.get("infos"),
        )
        print("Teste User-ReportValidation-9: Denúncia recusada com sucesso.")


class SuggestionValidationTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="Test User", password="userpassword"
        )
        self.moderator = User.objects.create_user(
            username="Test Moderator", password="moderatorpassword"
        )
        self.moderator.user_permissions.add(
            Permission.objects.get(codename="add_company")
        )
        self.suggestion = CompanySuggestionModel.objects.create(
            name="Test Suggestion",
            field_of_operation="Test FoP",
            link="https://teste.com",
            description="Teste Description",
            status="NV",
        )

    def test_pending_view_status_code(self):
        self.client.login(username="Test User", password="userpassword")
        response = self.client.get(reverse("user:pendingsuggestions"))
        self.assertEqual(response.status_code, 403)
        self.client.login(username="Test Moderator", password="moderatorpassword")
        response = self.client.get(reverse("user:pendingsuggestions"))
        self.assertEqual(response.status_code, 200)
        print("Teste User-SuggestionValidation-1: Acesso restringido com sucesso.")

    def test_validation_view_status_code(self):
        self.client.login(username="Test User", password="userpassword")
        response = self.client.get(
            reverse("user:suggestionvalidation", args=[self.suggestion.id])
        )
        self.assertEquals(response.status_code, 403)
        self.client.login(username="Test Moderator", password="moderatorpassword")
        response = self.client.get(
            reverse("user:suggestionvalidation", args=[self.suggestion.id])
        )
        self.assertEquals(response.status_code, 200)
        print("Teste User-SuggestionValidation-2: Acesso restringido com sucesso.")

    def test_pending_view_context(self):
        CompanySuggestionModel.objects.create(
            name="Test Suggestion 2",
            field_of_operation="Test FoP",
            link="https://teste.com",
            description="Teste Description",
            status="AP",
        )
        CompanySuggestionModel.objects.create(
            name="Test Suggestion 3",
            field_of_operation="Test FoP",
            link="https://teste.com",
            description="Teste Description",
            status="RE",
        )
        self.client.login(username="Test Moderator", password="moderatorpassword")
        response = self.client.get(reverse("user:pendingsuggestions"))
        self.assertSequenceEqual(
            response.context.get("suggestion_list"), [self.suggestion]
        )
        print(
            "Teste User-SuggestionValidation-3: Variáveis de contexto verificadas com sucesso."
        )

    def test_validation_suggestion_valid(self):
        form = ValidateSuggestionForm(
            {
                "action": "1",
                "name": ".",
                "description": ".",
                "logo": "company/logo/21/09/16/test_logo.png",
            }
        )
        form.is_valid()
        self.assertDictEqual(form.errors, {})
        print("Teste User-SuggestionValidation-4: Feedback enviado com sucesso.")

    def test_validation_action_in_form(self):
        form = ValidateSuggestionForm(
            {
                "name": ".",
                "description": ".",
                "logo": "company/logo/21/09/16/test_logo.png",
            }
        )
        form.is_valid()
        self.assertIn("action", form.errors)
        print("Teste User-SuggestionValidation-5: Ação inválida negada com sucesso.")

    def test_validation_name_in_form(self):
        form = ValidateSuggestionForm(
            {
                "action": "1",
                "description": ".",
                "logo": "company/logo/21/09/16/test_logo.png",
            }
        )
        form.is_valid()
        self.assertIn("name", form.errors)
        print("Teste User-SuggestionValidation-6: Nome inválido negado com sucesso.")

    def test_validation_description_in_form(self):
        form = ValidateSuggestionForm(
            {
                "action": "1",
                "name": ".",
                "logo": "company/logo/21/09/16/test_logo.png",
            }
        )
        form.is_valid()
        self.assertIn("description", form.errors)
        print(
            "Teste User-SuggestionValidation-7: Descrição inválida negada com sucesso."
        )

    def test_can_approve_suggestion(self):
        self.client.login(username="Test Moderator", password="moderatorpassword")
        self.client.post(
            reverse("user:suggestionvalidation", args=[self.suggestion.id]),
            data={
                "action": "1",
                "name": ".",
                "description": ".",
                "logo": SimpleUploadedFile(
                    name="pensenisso.png",
                    content=open("base_static/images/pensenisso.png", "rb").read(),
                    content_type="image/png",
                ),
            },
        )
        # check if the suggestion's status was changed successfully
        self.suggestion.refresh_from_db()
        self.assertEquals(self.suggestion.status, "AP")
        # check if the suggestion is no longer on pending suggestions list
        response = self.client.get(reverse("user:pendingsuggestions"))
        self.assertNotIn(self.suggestion, response.context.get("suggestion_list"))
        # check if the suggestion appears on company explorer
        response = self.client.get(reverse("search:explorer"))
        self.assertEquals(len(response.context.get("company_list")), 1)
        print("Teste User-SuggestionValidation-8: Empresa adicionada com sucesso.")

    def test_can_deny_suggestion(self):
        self.client.login(username="Test Moderator", password="moderatorpassword")
        self.client.post(
            reverse("user:suggestionvalidation", args=[self.suggestion.id]),
            data={"action": "0", "name": ".", "description": "."},
        )
        # check if the suggestion's status was changed successfully
        self.suggestion.refresh_from_db()
        self.assertEquals(self.suggestion.status, "RE")
        # check if the suggestion is no longer on pending suggestions list
        response = self.client.get(reverse("user:pendingsuggestions"))
        self.assertNotIn(self.suggestion, response.context.get("suggestion_list"))
        # check if the suggestion doesn't appear on company explorer
        response = self.client.get(reverse("search:explorer"))
        self.assertEquals(len(response.context.get("company_list")), 0)
        print("Teste User-SuggestionValidation-9: Sugestão recusada com sucesso.")
