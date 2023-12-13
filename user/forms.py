from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ValidateReportForm(forms.Form):
    gravity = forms.ChoiceField(
        choices=(("1", "Leve"), ("2", "Moderada"), ("3", "Grave"), ("4", "Gravíssima")),
        label="Gravidade:",
    )
    action = forms.ChoiceField(
        choices=(("1", "Aprovar"), ("0", "Recusar")),
        label="Ação:",
        widget=forms.RadioSelect,
    )
    feedback = forms.CharField(
        label="Feedback:", widget=forms.Textarea(attrs={"cols": "45", "rows": "8"})
    )

    class Meta:
        fields = ("gravity", "action", "feedback")


class ValidateSuggestionForm(forms.Form):
    action = forms.ChoiceField(
        choices=(("1", "Aprovar"), ("0", "Recusar")),
        label="Ação:",
        widget=forms.RadioSelect,
    )
    description = forms.CharField(
        label="Descrição da Empresa (se aprovada):",
        widget=forms.Textarea(attrs={"cols": "45", "rows": "8"}),
        required=False,
    )
    logo = forms.ImageField(label="Logo da Empresa (se aprovada):", required=False)

    class Meta:
        fields = ("action", "description", "logo")
