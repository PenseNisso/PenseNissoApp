from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    favorite_companies = models.ManyToManyField(
        "company.Company", related_name="favorites", blank=True
    )
