from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ValidateReportForm(forms.Form):
    feedback = forms.ChoiceField(
        choices=(("1", "Aprovar"), ("0", "Recusar")),
        label="Ação:",
        widget=forms.RadioSelect,
    )

    class Meta:
        fields = ("feedback",)
