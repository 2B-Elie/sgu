from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from .models import Patient, Doctor, Diagnosis, FirstAid
from .forms import PatientForm, DoctorForm, DiagnosisForm, FirstAidForm, SignUpForm, SignInForm
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

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
            return redirect('home')  # Change to your home view

        return render(request, self.template_name, {'form': form})

class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'registration/login.html'



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'user/index.html'
    
    # # Méthode pour ajouter ou modifier le contexte
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['site_name'] = 'HEPTOU'
    #     context['welcome_message'] = 'Welcome to our home page!'
    #     return context

# Vues pour Patient
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'user/patient_form.html'
    success_url = reverse_lazy('patient_list')

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
    template_name = 'firstaid_list.html'
