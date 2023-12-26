from .models import video,Series_Name
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class SeriesModel(forms.ModelForm):
    class Meta:
        model = Series_Name
        fields = ['Name','poster','type','genre','detail']

class upload(forms.ModelForm):
    class Meta:
        model = video
        fields = ['title','slug','file','image','content']

        def clean(self):
            cleaned_data = super().clean()
            user = self.cleaned_data.get('user')  # Assuming you have a user field in your model

            if not user.is_superuser:
                raise forms.ValidationError("Only superusers can create this object.")

            return cleaned_data

class RegisterModel(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


        widgets = {
            'username': forms.TextInput(attrs={'class': 'finput'}),
            'first_name': forms.TextInput(attrs={'class': 'finput'}),
            'last_name': forms.TextInput(attrs={'class': 'finput'}),
            'email': forms.EmailInput(attrs={'class': 'finput'}),
            'password1': forms.PasswordInput(attrs={'class': 'finput'}),
            'password2': forms.PasswordInput(attrs={'class': 'finput'}),
        }

        # def clean_email(self):
        #     email = self.cleaned_data.get('email')
        #     if User.objects.filter(email=email).exists():
        #         raise forms.ValidationError('This email address is already in use.')
        #     return email



class LoginForm(AuthenticationForm):
        class Meta:
            model = User
            fields = ("username", "password")
        
        username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'finput'}),
    )
        password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'finput'}),
    )   
       
       

            