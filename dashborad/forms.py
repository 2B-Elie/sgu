from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from ckeditor.widgets import CKEditorWidget
from .models import Patient, Doctor, Diagnosis, FirstAid, Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    user_type = forms.ChoiceField(choices=[('patient', 'Patient'), ('doctor', 'Médecin')], label='Je suis un(e)')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'S\'inscrire'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')
        if commit:
            user.save()
            Profile.objects.create(user=user, user_type=user_type)
        return user

class PatientForm(forms.ModelForm):
    medical_history = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Patient
        fields = ['date_of_birth', 'emergency_contact', 'medical_history']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enregistrer'))

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['profile', 'specialty']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assurez-vous que le profil doit être un utilisateur de type 'doctor'
        self.fields['profile'].queryset = Profile.objects.filter(user_type='doctor')

class DiagnosisForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    prescribed_treatment = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Diagnosis
        fields = ['patient', 'doctor', 'description', 'prescribed_treatment']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enregistrer'))

class FirstAidForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FirstAid
        fields = ['title', 'description', 'source']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enregistrer'))

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Se connecter'))
