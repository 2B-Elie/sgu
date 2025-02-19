from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Medecin, Patient, Route, Domicile
from ckeditor.widgets import CKEditorWidget

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'})
    )
    ROLE_CHOICES = [
        ('medecin', 'Médecin'),
        ('patient', 'Patient'),
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label="Rôle"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d’utilisateur'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}),
        }

class MedecinProfileForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['specialty', 'hospital_affiliation', 'license_number', 'contact_number']
        widgets = {
            'specialty': CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Spécialité'}),
            'hospital_affiliation': CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Affiliation Hospitalière'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de Licence'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de Contact'}),
        }

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['birth_date', 'medical_history', 'emergency_contact_name', 'emergency_contact_phone', 'chronic_conditions']
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de Naissance', 'type': 'date'}),
            'medical_history': CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Historique Médical'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du Contact d\'Urgence'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro du Contact d\'Urgence'}),
            'chronic_conditions': CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Conditions Chroniques'}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d’utilisateur'}),
        label="Nom d’utilisateur",
        max_length=254
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
        label="Mot de passe"
    )

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['title', 'description', 'steps']
        widgets = {
            'description': CKEditorWidget(),
            'steps': CKEditorWidget(),
        }
        labels = {
            'title': "Titre",
            'description': "Description",
            'steps': "Étapes",
        }
        help_texts = {
            'title': "Titre de la route de premiers secours.",
            'description': "Description détaillée de la route de premiers secours.",
            'steps': "Étapes à suivre pour fournir les premiers secours.",
        }

class DomicileForm(forms.ModelForm):
    class Meta:
        model = Domicile
        fields = ['symptom', 'explanation', 'assistance_method']
        widgets = {
            'explanation': CKEditorWidget(),
            'assistance_method': CKEditorWidget(),
        }
        labels = {
            'symptom': "Symptôme",
            'explanation': "Explication",
            'assistance_method': "Méthode d'assistance",
        }
        help_texts = {
            'symptom': "Symptôme observé qui nécessite une assistance à domicile.",
            'explanation': "Explication du symptôme et des raisons possibles.",
            'assistance_method': "Méthode ou procédure pour assister la personne à domicile.",
        }

class PatientUpdateForm(forms.ModelForm):
    medical_history = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Historique Médical'}),
        label="Historique Médical",
        required=False
    )
    chronic_conditions = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Conditions Chroniques'}),
        label="Conditions Chroniques",
        required=False
    )

    class Meta:
        model = Patient
        fields = ['medical_history', 'chronic_conditions']
class PatientSearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rechercher par nom'})
    )

class PatientAdmissionForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['user', 'birth_date', 'medical_history', 'emergency_contact_name', 'emergency_contact_phone', 'chronic_conditions']

class MedecinAdmissionForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['user', 'specialty', 'hospital_affiliation', 'license_number', 'contact_number']