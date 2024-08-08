from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from .models import Patient, Doctor, Diagnosis, FirstAid, Profile
from .forms import PatientForm, DoctorForm, DiagnosisForm, FirstAidForm, SignUpForm, SignInForm
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout


class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            try:
                profile = user.profile
                if profile.user_type == 'patient':
                    # Assurez-vous que le patient est bien créé
                    patient = Patient.objects.get(profile=profile)
                    return redirect('patient_update', pk=patient.id)  # Redirige vers la page de mise à jour du patient
                elif profile.user_type == 'doctor':
                    # Assurez-vous que le médecin est bien créé
                    doctor = Doctor.objects.get(profile=profile)
                    return redirect('doctor_update', pk=doctor.id)  # Redirige vers la page de mise à jour du médecin
            except (Patient.DoesNotExist, Doctor.DoesNotExist):
                # Gérer le cas où le profil n'est pas encore associé à un patient ou médecin
                return redirect('home')  # Redirection vers une page d'accueil ou une autre page pertinente

        return render(request, self.template_name, {'form': form})

class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'registration/login.html'

def custom_logout_view(request):
    logout(request)
    return redirect('login')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'user/index.html'

# Vues pour Patient
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'user/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.profile = profile
        return super().form_valid(form)

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'user/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'user/patient_detail.html'

class PatientListView(ListView):
    model = Patient
    template_name = 'user/patient_list.html'

# Vues pour Doctor
class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'user/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'user/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'user/doctor_detail.html'

class DoctorListView(ListView):
    model = Doctor
    template_name = 'user/doctor_list.html'

# Vues pour Diagnosis
class DiagnosisCreateView(CreateView):
    model = Diagnosis
    form_class = DiagnosisForm
    template_name = 'user/diagnosis_form.html'
    success_url = reverse_lazy('diagnosis_list')

class DiagnosisUpdateView(UpdateView):
    model = Diagnosis
    form_class = DiagnosisForm
    template_name = 'user/diagnosis_form.html'
    success_url = reverse_lazy('diagnosis_list')

class DiagnosisDetailView(DetailView):
    model = Diagnosis
    template_name = 'user/diagnosis_detail.html'

class DiagnosisListView(ListView):
    model = Diagnosis
    template_name = 'user/diagnosis_list.html'

# Vues pour FirstAid
class FirstAidCreateView(CreateView):
    model = FirstAid
    form_class = FirstAidForm
    template_name = 'user/firstaid_form.html'
    success_url = reverse_lazy('firstaid_list')

class FirstAidUpdateView(UpdateView):
    model = FirstAid
    form_class = FirstAidForm
    template_name = 'user/firstaid_form.html'
    success_url = reverse_lazy('firstaid_list')

class FirstAidDetailView(DetailView):
    model = FirstAid
    template_name = 'user/firstaid_detail.html'

class FirstAidListView(ListView):
    model = FirstAid
    template_name = 'user/firstaid_list.html'
