from django.apps import AppConfig
from django.db.utils import OperationalError


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self) -> None:
        try:
            from django.contrib.auth.models import Group, Permission
            from django.contrib.contenttypes.models import ContentType

            from company.models import Company
            from infos.models import Report

            moderator_group, created = Group.objects.get_or_create(name="Moderator")
            content_types = ContentType.objects.get_for_models(Report, Company).values()
            permissions = Permission.objects.filter(content_type__in=content_types)
            for perm in permissions:
                moderator_group.permissions.add(perm)
        except OperationalError:
            pass
