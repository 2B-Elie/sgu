from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class Medecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(
        max_length=255, 
        verbose_name=_("Spécialité"),
        help_text=_("Entrez la spécialité médicale du médecin, par exemple : Cardiologue, Dermatologue, etc.")
    )
    hospital_affiliation = models.CharField(
        max_length=255, 
        verbose_name=_("Affiliation Hospitalière"),
        blank=True, 
        null=True,
        help_text=_("Nom de l'hôpital ou de la clinique où le médecin est affilié.")
    )
    license_number = models.CharField(
        max_length=255, 
        verbose_name=_("Numéro de Licence"),
        help_text=_("Entrez le numéro de licence professionnelle du médecin.")
    )
    contact_number = models.CharField(
        max_length=20,  # Augmenté pour tenir compte des formats internationaux
        verbose_name=_("Numéro de Contact"),
        blank=True, 
        null=True,
        help_text=_("Numéro de téléphone ou de contact professionnel du médecin.")
    )
    profil_complet = models.BooleanField(default=False, verbose_name=_("Profil complet"))

    def __str__(self):
        return f"Dr. {self.user.username} - {self.specialty}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(
        verbose_name=_("Date de Naissance"),
        help_text=_("Entrez la date de naissance du patient."),
        blank=True, 
        null=True,

    )
    medical_history = models.TextField(
        verbose_name=_("Historique Médical"),
        blank=True, 
        null=True,
        help_text=_("Entrez un résumé des antécédents médicaux du patient, y compris les maladies chroniques, les opérations, etc.")
    )
    emergency_contact_name = models.CharField(
        max_length=255, 
        verbose_name=_("Nom du Contact d'Urgence"),
        help_text=_("Entrez le nom de la personne à contacter en cas d'urgence.")
    )
    emergency_contact_phone = models.CharField(
        max_length=20,  # Augmenté pour tenir compte des formats internationaux
        verbose_name=_("Numéro du Contact d'Urgence"),
        help_text=_("Entrez le numéro de téléphone de la personne à contacter en cas d'urgence.")
    )
    chronic_conditions = models.CharField(
        max_length=255, 
        verbose_name=_("Conditions Chroniques"),
        blank=True, 
        null=True,
        help_text=_("Entrez les conditions médicales chroniques du patient, par exemple : Diabète, Hypertension, etc.")
    )
    profil_complet = models.BooleanField(default=False, verbose_name=_("Profil complet"))

    def __str__(self):
        return self.user.username

class Route(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Titre"),
        help_text=_("Titre de la route de premiers secours.")
    )
    description = RichTextField(
        verbose_name=_("Description"),
        help_text=_("Description détaillée de la route de premiers secours.")
    )
    steps = RichTextField(
        verbose_name=_("Étapes"),
        help_text=_("Étapes à suivre pour fournir les premiers secours.")
    )

    def __str__(self):
        return self.title

class Domicile(models.Model):
    symptom = models.CharField(
        max_length=255,
        verbose_name=_("Symptôme"),
        help_text=_("Symptôme observé qui nécessite une assistance à domicile.")
    )
    explanation = RichTextField(
        verbose_name=_("Explication"),
        help_text=_("Explication du symptôme et des raisons possibles.")
    )
    assistance_method = RichTextField(
        verbose_name=_("Méthode d'assistance"),
        help_text=_("Méthode ou procédure pour assister la personne à domicile.")
    )

    def __str__(self):
        return self.symptom