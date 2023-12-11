from django import forms


class CompanySuggestion(forms.Form):
    choices_has_info = [("none", "-"), ("yes", "Sim"), ("no", "Não")]

    name = forms.CharField(max_length=100, label="Nome da Empresa:")
    description = forms.CharField(
        max_length=400,
        widget=forms.Textarea(),
        label="Descrição sobre a empresa e sua área de atuação.",
    )
