from django.contrib import admin
from .models import Patient, Doctor, Diagnosis, FirstAid
from ckeditor.widgets import CKEditorWidget
from django.db import models

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'emergency_contact')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'emergency_contact')
    list_filter = ('date_of_birth',)
    fieldsets = (
        (None, {
            'fields': ('user', 'date_of_birth', 'emergency_contact', 'medical_history')
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'specialty')
    list_filter = ('specialty',)
    fieldsets = (
        (None, {
            'fields': ('user', 'specialty')
        }),
    )


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'description')
    search_fields = ('patient__user__username', 'doctor__user__username', 'description')
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
