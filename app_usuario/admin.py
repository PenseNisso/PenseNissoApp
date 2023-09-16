from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario

# só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(("Empresas favoritas:", {"fields": ("empresas_favoritas",)}))
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Usuario, UserAdmin)
