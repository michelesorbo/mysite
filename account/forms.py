from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Ripeti Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']

        #Controllo l'esattezza della seconda password
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Le password non coincidono')
            return cd['password2']
        
        #Verifico se la mail è già presente nel DB
        def clean_email(self):
            data = self.cleaned_data['email']
            if User.objects.filter(email=data).exists(): #Controllo se l'email inserita è già presente nel DB
                raise forms.ValidationError('Email già presente')
            return data