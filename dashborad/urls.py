# your_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from .views import (
    HomeView, SignUpView, ProfileCompleteView,ProfileUpdateView, 
    CustomLoginView, MedecinDashboardView, PatientDashboardView,
    RouteCreateView, RouteUpdateView, RouteDetailView, RouteListView, 
    DomicileCreateView, DomicileUpdateView, DomicileDetailView, 
    DomicileListView, update_patient_profile,PatientListView, PatientDetailView,
    PavillonView, patient_admission, SuccessPage, UsagersView
    )


urlpatterns = [

    path('', HomeView.as_view(), name='home'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('complete-profile/', ProfileCompleteView.as_view(), name='profile_complete'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('medecin-dashboard/', MedecinDashboardView.as_view(), name='medecin_dashboard'),
    path('patient-dashboard/', PatientDashboardView.as_view(), name='patient_dashboard'),  

    # URLs pour le modèle Route
    path('route/create/', RouteCreateView.as_view(), name='route_create'),
    path('route/<int:pk>/update/', RouteUpdateView.as_view(), name='route_update'),
    path('route/<int:pk>/', RouteDetailView.as_view(), name='route_detail'),
    path('routes/', RouteListView.as_view(), name='route_list'),

    # URLs pour le modèle Domicile
    path('domicile/create/', DomicileCreateView.as_view(), name='domicile_create'),
    path('domicile/<int:pk>/update/', DomicileUpdateView.as_view(), name='domicile_update'),
    path('domicile/<int:pk>/', DomicileDetailView.as_view(), name='domicile_detail'),
    path('domiciles/', DomicileListView.as_view(), name='domicile_list'),

    # URLs pour Usagers
    path('usagers/informations-medicale/', update_patient_profile, name='update_profile'),
    path('usagers/', UsagersView.as_view(), name='usagers'),
    path('usagers/recherche/<str:query>/', PatientListView.as_view(), name='patient_search_results'),

    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),

    # Urls pour Pavillon
    path('pavillon/', PavillonView.as_view(), name='pavillon'),
    path('admission/', patient_admission, name='patient_admission'),
    path('success/', SuccessPage.as_view(), name='success_page'),
]
