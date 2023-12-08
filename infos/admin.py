from django.contrib import admin

from .models import Lawsuit, News, Report, ReportCategory


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "status")
    list_filter = ("status",)

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "title",
                    "content",
                    "company",
                    "category",
                    "links",
                    "date",
                    "user",
                ]
            },
        ),
        ("Moderation", {"fields": ["gravity", "status", "feedback"]}),
    ]


admin.site.register(ReportCategory)
admin.site.register(News)
admin.site.register(Lawsuit)
