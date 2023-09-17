from django.contrib import admin

from .models import Company, Report, ReportCategory

admin.site.register(Report)
admin.site.register(ReportCategory)
admin.site.register(Company)
