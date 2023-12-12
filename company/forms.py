from django import forms


class CompanySuggestion(forms.Form):
    name = forms.CharField(max_length=100, label="Nome da Empresa:", required=True)
    field_of_operation = forms.CharField(
        max_length=50, label="Área de Atuação:", required=True
    )
    link = forms.URLField(max_length=30, required=False)

    description = forms.CharField(
        max_length=400,
        widget=forms.Textarea(),
        label="Descrição sobre a empresa e sua área de atuação:",
        required=False,
    )
