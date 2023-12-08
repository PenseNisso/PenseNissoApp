# Generated by Django 4.2.5 on 2023-11-30 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0002_alter_company_options"),
        ("infos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to="company.company",
            ),
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("author", models.CharField(max_length=50)),
                ("date", models.DateField()),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="news",
                        to="company.company",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "News",
            },
        ),
    ]
