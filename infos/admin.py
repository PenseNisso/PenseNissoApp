from django.contrib import admin

from .models import Report, ReportCategory

admin.site.register(Report)
admin.site.register(ReportCategory)
