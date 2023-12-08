# Generated by Django 4.2.5 on 2023-12-08 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_options'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_companies',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='company.company'),
        ),
    ]
