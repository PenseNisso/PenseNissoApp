from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Include "favorite_companies" field in admin view.
fields = list(UserAdmin.fieldsets)
fields.append(("Empresas favoritas:", {"fields": ("favorite_companies",)}))
UserAdmin.fieldsets = tuple(fields)

# Register your models here.
admin.site.register(User, UserAdmin)
