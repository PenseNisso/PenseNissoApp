from django.db import models
from django.utils.timezone import now
import math


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

    class Meta:
        verbose_name_plural = "Companies"
