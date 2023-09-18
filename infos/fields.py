from django.db.models.base import Model
from django.forms import ModelChoiceField

from company.models import Company
from .models import ReportCategory


class ReportCategoryModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj: ReportCategory) -> str:
        return obj.formatted_name


class CompanyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj: Company) -> str:
        return obj.name
