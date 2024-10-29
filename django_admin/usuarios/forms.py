from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model= User
        fields= ('username', 'email', 'password','password2')
        
        def save(self, commit=True): 
            user= super(RegistroUsuarioForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            
            if commit:
                user.save()
            return use
        
class LoginUsuarioForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'}))

    class Meta:
        model = User
        fields = ['email', 'password']
