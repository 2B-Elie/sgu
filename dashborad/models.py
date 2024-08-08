from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Médecin'),
    ]
    GENDER_CHOICES = [
        ('male', 'Homme'),
        ('female', 'Femme'),
        ('other', 'Autre'),
        ('prefer_not_to_say', 'Préférer ne pas dire'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='patient')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True, verbose_name=_("Sexe"))

    class Meta:
        verbose_name = _("Profil")
        verbose_name_plural = _("Profils")

    def __str__(self):
        return f"Profil de {self.user.username}"

class Patient(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'patient'}, verbose_name=_("Profil"))
    date_of_birth = models.DateField(verbose_name=_("Date de naissance"), help_text=_("La date de naissance du patient"))
    emergency_contact = models.CharField(max_length=100, verbose_name=_("Contact d'urgence"), help_text=_("Personne à contacter en cas d'urgence"))
    medical_history = models.TextField(blank=True, null=True, verbose_name=_("Antécédents médicaux"), help_text=_("Historique médical du patient"))

    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"

class Doctor(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'}, verbose_name=_("Profil"))
    specialty = models.CharField(max_length=100, verbose_name=_("Spécialité"), help_text=_("Spécialité du médecin"))

    class Meta:
        verbose_name = _("Médecin")
        verbose_name_plural = _("Médecins")

    def __str__(self):
        return f"Dr. {self.profile.user.first_name} {self.profile.user.last_name} - {self.specialty}"

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnoses', verbose_name=_("Patient"))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name=_("Médecin"))
    date = models.DateField(auto_now_add=True, verbose_name=_("Date"), help_text=_("Date du diagnostic"))
    description = RichTextField(verbose_name=_("Description"), help_text=_("Description du diagnostic"))
    prescribed_treatment = RichTextField(verbose_name=_("Traitement prescrit"), help_text=_("Traitement prescrit au patient"))

    class Meta:
        verbose_name = _("Diagnostic")
        verbose_name_plural = _("Diagnostics")
        indexes = [
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"Diagnostic pour {self.patient} par {self.doctor} le {self.date}"

class FirstAid(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Titre"), help_text=_("Titre de l'assistance de premiers secours"))
    description = RichTextField(verbose_name=_("Description"), help_text=_("Description des premiers secours"))
    source = models.URLField(validators=[URLValidator()], verbose_name=_("Source"), help_text=_("Lien vidéo expliquant les étapes des premiers secours"))

    class Meta:
        verbose_name = _("Premiers Secours")
        verbose_name_plural = _("Premiers Secours")

    def __str__(self):
        return f"Premiers Secours: {self.title}"
