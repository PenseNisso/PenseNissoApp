from django.contrib import admin
from .models import Report, ReportCategory
from .models import Company

admin.site.register(Report)
admin.site.register(ReportCategory)
admin.site.register(Company)
