from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class LengthValidator:
    def __init__(self, min_length=8, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):
        size = len(password)
        if size < self.min_length:
            raise ValidationError(
                _("Sua senha deve conter no mínimo %(min_length)d caracteres."),
                code="password_too_short",
                params={"min_length": self.min_length},
            )
        if size > self.max_length:
            raise ValidationError(
                _("Sua senha deve conter no máximo %(max_length)d caracteres."),
                code="password_too_long",
                params={"max_length": self.max_length},
            )

    def get_help_text(self):
        return _(
            f"Sua senha deve conter entre {self.min_length} e {self.max_length} caracteres."
        )


class CaseValidator:
    def validate(self, password: str, user=None):
        uppercase = [ch.isupper() for ch in password if ch.isalpha()]
        if not any(uppercase):
            raise ValidationError(
                _("Essa senha não contém nenhuma letra maiúscula."),
                code="password_without_uppercase",
            )
        if all(uppercase):
            raise ValidationError(
                _("Essa senha não contém nenhuma letra minúscula."),
                code="password_without_lowercase",
            )

    def get_help_text(self):
        return _("Sua senha precisa conter letras maiúsculas e minúsculas.")


class NumericValidator:
    def validate(self, password: str, user=None):
        for ch in password:
            if ch.isnumeric():
                return
        raise ValidationError(
            _("Essa senha não contém números."),
            code="password_without_number",
        )

    def get_help_text(self):
        return _("Sua senha precisa conter números.")


class SpecialCharacterValidator:
    special_characters = "'\"!@#$%&*-_=+;:?"

    def validate(self, password: str, user=None):
        for ch in password:
            if ch in self.special_characters:
                return
        raise ValidationError(
            _("Essa senha não contém caracteres especiais."),
            code="password_without_special_characters",
        )

    def get_help_text(self):
        return _(
            f"Sua senha precisa conter caracteres especiais ({'/'.join(self.special_characters)})."
        )
