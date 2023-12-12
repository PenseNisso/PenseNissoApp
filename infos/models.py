from django.db import models


class InfoBase(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        abstract = True


class Report(InfoBase):
    company = models.ForeignKey(
        "company.Company", on_delete=models.CASCADE, related_name="reports"
    )
    category = models.ForeignKey("ReportCategory", on_delete=models.SET_NULL, null=True)
    links = models.TextField()
    user = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reports_sent",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[("RE", "Recusado"), ("NV", "Não verificado"), ("AP", "Aprovado")],
        default="NV",
    )
    gravity = models.CharField(
        max_length=20,
        choices=[("1", "Leve"), ("2", "Moderada"), ("3", "Grave"), ("4", "Gravíssima")],
        default="1",
    )
    date = models.DateField(default="1970-01-01")
    feedback = models.TextField(blank=True)


class ReportCategory(models.Model):
    name = models.CharField(max_length=100)
    formatted_name = models.CharField(max_length=100, default="Categoria")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Report categories"


class Lawsuit(InfoBase):
    company = models.ForeignKey(
        "company.Company", on_delete=models.CASCADE, related_name="lawsuits"
    )
    source = models.URLField()
    start_year = models.PositiveSmallIntegerField()
    resolution_year = models.PositiveSmallIntegerField(null=True, blank=True)


class News(InfoBase):
    company = models.ForeignKey(
        "company.Company", on_delete=models.CASCADE, related_name="news"
    )
    author = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to="news_banners")

    class Meta:
        verbose_name_plural = "News"
