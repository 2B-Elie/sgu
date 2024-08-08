from django.contrib import admin
from .models import Patient, Doctor, Diagnosis, FirstAid, Profile
from ckeditor.widgets import CKEditorWidget
from django.db import models

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'gender')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user_type', 'gender')
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('profile', 'date_of_birth', 'emergency_contact')
    list_filter = ('date_of_birth',)
    fieldsets = (
        (None, {
            'fields': ('profile', 'date_of_birth', 'emergency_contact', 'medical_history')
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('profile', 'specialty')
    list_filter = ('specialty',)
    fieldsets = (
        (None, {
            'fields': ('profile', 'specialty')
        }),
    )

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'description')
    search_fields = ('patient__profile__user__username', 'doctor__profile__user__username', 'description')
    list_filter = ('date',)
    fieldsets = (
        (None, {
            'fields': ('patient', 'doctor', 'description', 'prescribed_treatment')
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

@admin.register(FirstAid)
class FirstAidAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'source')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'source')
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
