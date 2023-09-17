from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("ReportCategory", on_delete=models.SET_NULL, null=True)
    links = models.TextField()
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ReportCategory(models.Model):
    name = models.CharField(max_length=100)
    formatted_name = models.CharField(max_length=100, default="Categoria")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Report categories"


class Company(models.Model):
    name = models.CharField(max_length=100)
