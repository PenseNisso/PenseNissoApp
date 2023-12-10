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
    feedback = forms.CharField(label="Feedback:", widget=forms.Textarea(attrs = {"cols": "45", "rows": "8"}))

    class Meta:
        fields = ("gravity", "action", "feedback")
