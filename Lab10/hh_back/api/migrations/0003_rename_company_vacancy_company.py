# Generated by Django 5.1.7 on 2025-04-03 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_company_options_alter_vacancy_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vacancy",
            old_name="Company",
            new_name="company",
        ),
    ]
