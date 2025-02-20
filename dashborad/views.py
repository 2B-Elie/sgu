from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login as auth_login
from .models import Medecin, Patient, Route, Domicile
from .forms import SignUpForm, MedecinProfileForm, PatientProfileForm, CustomLoginForm, DomicileForm, RouteForm, PatientUpdateForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'user/index.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        
        # Vérifiez le rôle de l'utilisateur et redirigez vers le tableau de bord approprié
        if hasattr(user, 'medecin'):
            return redirect('medecin_dashboard')  # Remplacez 'medecin_dashboard' par le nom de l'URL du tableau de bord du médecin
        elif hasattr(user, 'patient'):
            return redirect('patient_dashboard')  # Remplacez 'patient_dashboard' par le nom de l'URL du tableau de bord du patient
        else:
            return super().get(request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')  # Redirige vers la page de connexion après l'inscription

    def form_valid(self, form):
        response = super().form_valid(form)
        role = form.cleaned_data.get('role')
        user = self.object

        if role == 'medecin':
            Medecin.objects.create(user=user)
        elif role == 'patient':
            Patient.objects.create(user=user)

        return response

class ProfileCompleteView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile_complete.html'
    
    def get_object(self):
        user = self.request.user
        if hasattr(user, 'medecin'):
            return user.medecin
        elif hasattr(user, 'patient'):
            return user.patient
        return None

    def get_form_class(self):
        user = self.request.user
        if hasattr(user, 'medecin'):
            return MedecinProfileForm
        elif hasattr(user, 'patient'):
            return PatientProfileForm
        return None

    def get(self, request, *args, **kwargs):
        # Vérifiez si le profil est déjà complet
        if hasattr(request.user, 'medecin') and request.user.medecin.profil_complet:
            return redirect('medecin_dashboard')
        elif hasattr(request.user, 'patient') and request.user.patient.profil_complet:
            return redirect('patient_dashboard')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Mettre à jour l'état de profil_complet
        profile = self.object
        profile.profil_complet = True
        profile.save()

        return response

    def get_success_url(self):
        if hasattr(self.request.user, 'medecin'):
            return reverse_lazy('medecin_dashboard')
        elif hasattr(self.request.user, 'patient'):
            return reverse_lazy('patient_dashboard')
        return reverse_lazy('home')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)

        # Vérifiez si l'utilisateur a déjà complété son profil
        if hasattr(user, 'medecin'):
            if user.medecin.profil_complet:
                return redirect('medecin_dashboard')
            else:
                return redirect('profile_complete')
        elif hasattr(user, 'patient'):
            if user.patient.profil_complet:
                return redirect('patient_dashboard')
            else:
                return redirect('profile_complete')

        return redirect('home')  # Redirige vers la page d'accueil si aucun profil n'est trouvé

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile_update.html'
    
    def get_object(self):
        # Récupère l'utilisateur connecté
        user = self.request.user
        if hasattr(user, 'medecin'):
            return user.medecin
        elif hasattr(user, 'patient'):
            return user.patient
        return None

    def get_form_class(self):
        # Sélectionne le formulaire en fonction du type de l'utilisateur
        user = self.request.user
        if hasattr(user, 'medecin'):
            return MedecinProfileForm
        elif hasattr(user, 'patient'):
            return PatientProfileForm
        return None

    def get_success_url(self):
        # Redirige vers le dashboard approprié après la mise à jour du profil
        if hasattr(self.request.user, 'medecin'):
            return reverse_lazy('medecin_dashboard')
        elif hasattr(self.request.user, 'patient'):
            return reverse_lazy('patient_dashboard')
        return reverse_lazy('home')

    def form_valid(self, form):
        # Change l'état du profil à complet si tous les champs obligatoires sont remplis
        profil = form.save(commit=False)
        profil.profil_complet = self.check_profil_complet(profil)
        profil.save()
        return super().form_valid(form)

    def check_profil_complet(self, profil):
        # Vérifie si tous les champs obligatoires sont remplis
        if isinstance(profil, Medecin):
            return all([
                profil.specialty,
                profil.license_number,
            ])
        elif isinstance(profil, Patient):
            return all([
                profil.birth_date,
                profil.emergency_contact_name,
                profil.emergency_contact_phone,
            ])
        return False

class MedecinDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/medecin_dashboard.html'

class PatientDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/patient_dashboard.html'


class RouteCreateView(CreateView):
    model = Route
    form_class = RouteForm
    template_name = 'route/route_form.html'
    success_url = reverse_lazy('route_list')

class RouteUpdateView(UpdateView):
    model = Route
    form_class = RouteForm
    template_name = 'route/route_form.html'
    success_url = reverse_lazy('route_list')

class RouteDetailView(DetailView):
    model = Route
    template_name = 'route/route_detail.html'
    context_object_name = 'route'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_medecin'] = hasattr(user, 'medecin')
        return context    

class RouteListView(ListView):
    model = Route
    template_name = 'route/route_list.html'
    context_object_name = 'routes'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_medecin'] = hasattr(user, 'medecin')
        return context



class DomicileCreateView(CreateView):
    model = Domicile
    form_class = DomicileForm
    template_name = 'domicile/domicile_form.html'
    success_url = reverse_lazy('domicile_list')

class DomicileUpdateView(UpdateView):
    model = Domicile
    form_class = DomicileForm
    template_name = 'domicile/domicile_form.html'
    success_url = reverse_lazy('domicile_list')

class DomicileDetailView(DetailView):
    model = Domicile
    template_name = 'domicile/domicile_detail.html'
    context_object_name = 'domicile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_medecin'] = hasattr(user, 'medecin')
        return context    

class DomicileListView(ListView):
    model = Domicile
    template_name = 'domicile/domicile_list.html'
    context_object_name = 'domiciles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_medecin'] = hasattr(user, 'medecin')
        return context
    

@login_required
def update_patient_profile(request):
    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        return redirect('home')  # Ou une autre page si le patient n'existe pas

    full_name = f"{request.user.first_name} {request.user.last_name}"
    full_name = f"{request.user.first_name} {request.user.last_name}"
    emergency_contact_name = f"{patient.emergency_contact_name}"
    emergency_contact_phone = f"{patient.emergency_contact_phone}"


    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige vers une page de profil ou de succès
    else:
        form = PatientUpdateForm(instance=patient)

    context = {
        'form': form,
        'full_name': full_name,
        'emergency_contact_name': emergency_contact_name,
        'emergency_contact_phone': emergency_contact_phone,

    }

    return render(request, 'usagers/update_profile.html', context)

class PatientListView(ListView):
    model = Patient
    template_name = 'usagers/patient_list.html'
    context_object_name = 'patients'
    paginate_by = 10  # Nombre de patients par page

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(user__first_name__icontains=search_query) |
                Q(user__last_name__icontains=search_query)
            )
        return queryset

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'usagers/patient_detail.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.object
        context['full_name'] = patient.user.get_full_name()
        context['medical_history'] = patient.medical_history
        context['chronic_conditions'] = patient.chronic_conditions
        return context    

class PavillonView(TemplateView):
    template_name = 'pavillon/pavillon.html'


from django.shortcuts import render, redirect
from .forms import PatientAdmissionForm, MedecinAdmissionForm
from .models import Patient, Medecin

def patient_admission(request):
    if request.method == 'POST':
        patient_form = PatientAdmissionForm(request.POST)
        medecin_form = MedecinAdmissionForm(request.POST)
        if patient_form.is_valid() and medecin_form.is_valid():
            patient = patient_form.save()
            medecin = medecin_form.save()
            return redirect('success_page')  # Redirigez vers une page de succès
    else:
        patient_form = PatientAdmissionForm()
        medecin_form = MedecinAdmissionForm()
    
    return render(request, 'pavillon/patient_admission.html', {
        'patient_form': patient_form,
        'medecin_form': medecin_form,
    })

class SuccessPage(TemplateView):
    template_name = 'pavillon/success_page.html'


class UsagersView(TemplateView):
    template_name = 'usagers/usagers.html'    