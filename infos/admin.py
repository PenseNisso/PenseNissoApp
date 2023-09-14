from django.contrib import admin
from .models import ReportCategory, News, Report, Lawsuit, Company

# Register your models here.
admin.site.register(ReportCategory)
admin.site.register(News)
admin.site.register(Report)
admin.site.register(Lawsuit)
admin.site.register(Company)

