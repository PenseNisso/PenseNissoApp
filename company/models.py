import math

from django.db import models
from django.utils.timezone import now


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="company/logo/%y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def compute_score(self) -> float:
        reports = self.reports.filter(status="AP")
        sub_score = 0
        for report in reports:
            age = (now().date() - report.date).days / 365
            sub_score += math.exp(-2 * age / int(report.gravity))
        score = 5 - min(sub_score, 5)

        return round(score, 2)

    def compute_score_users(self) -> "float | str":
        rates = self.user_ratings.all()
        if len(rates) == 0:
            score_users = "--"
        else:
            sub_score_users = 0
            for rate in rates:
                sub_score_users += rate.score
            score_users = round(sub_score_users / len(rates), 2)
        return score_users

    class Meta:
        verbose_name_plural = "Companies"


class CompanySuggestionModel(models.Model):
    name = models.CharField(max_length=100)
    field_of_operation = models.CharField(max_length=50)
    link = models.URLField(max_length=30, null=True)
    description = models.TextField(max_length=400, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="suggestions_sent",
    )
    status = models.CharField(
        max_length=20,
        choices=[("RE", "Recusado"), ("NV", "Não verificado"), ("AP", "Aprovado")],
        default="NV",
    )


class Rate(models.Model):
    company = models.ForeignKey(
        "company.Company", on_delete=models.CASCADE, related_name="user_ratings"
    )
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="rated_companies"
    )
    score = models.IntegerField()
