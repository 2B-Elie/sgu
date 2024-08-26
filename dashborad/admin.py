from django.contrib import admin
from .models import Medecin, Patient, Route, Domicile
from ckeditor.widgets import CKEditorWidget
from django import forms

class MedecinAdminForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = '__all__'

class PatientAdminForm(forms.ModelForm):
    medical_history = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Patient
        fields = '__all__'

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    form = MedecinAdminForm
    list_display = ('user', 'specialty', 'contact_number', 'profil_complet')
    search_fields = ('user__username', 'specialty', 'license_number')
    list_filter = ('profil_complet',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = ('user', 'birth_date', 'emergency_contact_name', 'emergency_contact_phone', 'profil_complet')
    search_fields = ('user__username', 'emergency_contact_name')
    list_filter = ('profil_complet',)
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'steps')
        }),
    )

@admin.register(Domicile)
class DomicileAdmin(admin.ModelAdmin):
    list_display = ('symptom',)
    search_fields = ('symptom',)
    list_filter = ('symptom',)
    ordering = ('symptom',)
    fieldsets = (
        (None, {
            'fields': ('symptom', 'explanation', 'assistance_method')
        }),
    )
