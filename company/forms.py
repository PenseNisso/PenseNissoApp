from django import forms


class EvaluateForm(forms.Form):

    score = forms.ChoiceField(
        choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")),
        label="Avaliação",
        # widget=forms.RadioSelect
    )

