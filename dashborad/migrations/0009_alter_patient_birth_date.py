# Generated by Django 5.1 on 2024-08-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashborad", "0008_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="birth_date",
            field=models.DateField(
                blank=True,
                help_text="Entrez la date de naissance du patient.",
                null=True,
                verbose_name="Date de Naissance",
            ),
        ),
    ]
