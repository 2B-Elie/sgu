# Generated by Django 5.1 on 2024-08-08 08:26

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FirstAid",
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
                (
                    "title",
                    models.CharField(
                        help_text="Titre de l'assistance de premiers secours",
                        max_length=100,
                        verbose_name="Titre",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Description des premiers secours",
                        verbose_name="Description",
                    ),
                ),
                (
                    "source",
                    models.URLField(
                        help_text="Lien vidéo expliquant les étapes des premiers secours",
                        validators=[django.core.validators.URLValidator()],
                        verbose_name="Source",
                    ),
                ),
            ],
            options={
                "verbose_name": "Premiers Secours",
                "verbose_name_plural": "Premiers Secours",
            },
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "user_type",
                    models.CharField(
                        choices=[("patient", "Patient"), ("doctor", "Médecin")],
                        default="patient",
                        max_length=10,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("male", "Homme"),
                            ("female", "Femme"),
                            ("other", "Autre"),
                            ("prefer_not_to_say", "Préférer ne pas dire"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="Sexe",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Profil",
                "verbose_name_plural": "Profils",
            },
        ),
        migrations.CreateModel(
            name="Patient",
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
                (
                    "date_of_birth",
                    models.DateField(
                        help_text="La date de naissance du patient",
                        verbose_name="Date de naissance",
                    ),
                ),
                (
                    "emergency_contact",
                    models.CharField(
                        help_text="Personne à contacter en cas d'urgence",
                        max_length=100,
                        verbose_name="Contact d'urgence",
                    ),
                ),
                (
                    "medical_history",
                    models.TextField(
                        blank=True,
                        help_text="Historique médical du patient",
                        null=True,
                        verbose_name="Antécédents médicaux",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        limit_choices_to={"user_type": "patient"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashborad.profile",
                        verbose_name="Profil",
                    ),
                ),
            ],
            options={
                "verbose_name": "Patient",
                "verbose_name_plural": "Patients",
            },
        ),
        migrations.CreateModel(
            name="Doctor",
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
                (
                    "specialty",
                    models.CharField(
                        help_text="Spécialité du médecin",
                        max_length=100,
                        verbose_name="Spécialité",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        limit_choices_to={"user_type": "doctor"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashborad.profile",
                        verbose_name="Profil",
                    ),
                ),
            ],
            options={
                "verbose_name": "Médecin",
                "verbose_name_plural": "Médecins",
            },
        ),
        migrations.CreateModel(
            name="Diagnosis",
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
                (
                    "date",
                    models.DateField(
                        auto_now_add=True,
                        help_text="Date du diagnostic",
                        verbose_name="Date",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Description du diagnostic",
                        verbose_name="Description",
                    ),
                ),
                (
                    "prescribed_treatment",
                    ckeditor.fields.RichTextField(
                        help_text="Traitement prescrit au patient",
                        verbose_name="Traitement prescrit",
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashborad.doctor",
                        verbose_name="Médecin",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="diagnoses",
                        to="dashborad.patient",
                        verbose_name="Patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Diagnostic",
                "verbose_name_plural": "Diagnostics",
                "indexes": [
                    models.Index(fields=["date"], name="dashborad_d_date_743549_idx")
                ],
            },
        ),
    ]
