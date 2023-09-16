from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company

# from empresa.models import Empresa

class Usuario(AbstractUser):
    empresas_favoritas = models.ManyToManyField("Company")
