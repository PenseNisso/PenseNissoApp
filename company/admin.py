from django.contrib import admin

from company.models import Company, CompanySuggestionModel

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanySuggestionModel)
