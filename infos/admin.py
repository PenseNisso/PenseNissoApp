from django.contrib import admin

from .models import Lawsuit, News, Report, ReportCategory

admin.site.register(Report)
admin.site.register(ReportCategory)
admin.site.register(News)
admin.site.register(Lawsuit)
