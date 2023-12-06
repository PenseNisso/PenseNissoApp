from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self) -> None:
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType

        from infos.models import Report

        moderator_group, created = Group.objects.get_or_create(name="Moderator")
        content_type = ContentType.objects.get_for_model(Report)
        permissions = Permission.objects.filter(content_type=content_type)
        for perm in permissions:
            moderator_group.permissions.add(perm)
