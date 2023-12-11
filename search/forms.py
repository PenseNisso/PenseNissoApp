from typing import Any

from django import forms


class FilterForm(forms.Form):
    choices_has_info = [("none", "-"), ("yes", "Sim"), ("no", "Não")]

    has_reports = forms.ChoiceField(
        label="Tem denúncias",
        required=False,
        choices=choices_has_info,
        initial=choices_has_info[0],
    )
    has_news = forms.ChoiceField(
        label="Tem notícias",
        required=False,
        choices=choices_has_info,
        initial=choices_has_info[0],
    )
    has_lawsuits = forms.ChoiceField(
        label="Tem processos",
        required=False,
        choices=choices_has_info,
        initial=choices_has_info[0],
    )


class SortingForm(forms.Form):
    sorting_options = [
        ("alphabetical_ascending", "A-Z"),
        ("alphabetical_descending", "Z-A"),
        ("most_reports", "Mais Denúncias"),
        ("least_reports", "Menos Denúncias"),
        ("highest_score", "Maior Nota"),
        ("lowest_score", "Menor Nota"),
    ]

    sorting = forms.ChoiceField(
        label="Ordenar por:",
        required=False,
        choices=sorting_options,
        initial=sorting_options[0],
    )
