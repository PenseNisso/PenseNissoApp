from company.models import Company
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    empresas_favoritas = models.ManyToManyField("Company")
