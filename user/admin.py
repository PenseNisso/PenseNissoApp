from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CompaniesInline(admin.TabularInline):
    model = User.favorite_companies.through
    extra = 1


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (CompaniesInline,)
    base_fields = list(UserAdmin.fieldsets)
    base_fields.append(("Empresas favoritas:", {"fields": ("favorite_companies",)}))
    fieldsets = tuple(base_fields)
