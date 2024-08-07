# your_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    HomeView,SignUpView,SignInView,
    PatientCreateView, PatientUpdateView, PatientDetailView, PatientListView,
    DoctorCreateView, DoctorUpdateView, DoctorDetailView, DoctorListView,
    DiagnosisCreateView, DiagnosisUpdateView, DiagnosisDetailView, DiagnosisListView,
    FirstAidCreateView, FirstAidUpdateView, FirstAidDetailView, FirstAidListView
)

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', SignInView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', HomeView.as_view(), name='home'),

    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patients/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_update'),
    
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors/<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor_update'),
    
    path('diagnoses/', DiagnosisListView.as_view(), name='diagnosis_list'),
    path('diagnoses/create/', DiagnosisCreateView.as_view(), name='diagnosis_create'),
    path('diagnoses/<int:pk>/', DiagnosisDetailView.as_view(), name='diagnosis_detail'),
    path('diagnoses/<int:pk>/edit/', DiagnosisUpdateView.as_view(), name='diagnosis_update'),
    
    path('firstaids/', FirstAidListView.as_view(), name='firstaid_list'),
    path('firstaids/create/', FirstAidCreateView.as_view(), name='firstaid_create'),
    path('firstaids/<int:pk>/', FirstAidDetailView.as_view(), name='firstaid_detail'),
    path('firstaids/<int:pk>/edit/', FirstAidUpdateView.as_view(), name='firstaid_update'),    
]

