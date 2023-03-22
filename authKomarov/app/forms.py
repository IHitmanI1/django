from django import forms
from .models import User

class UserAuthenticationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', min_length= 3, max_length=50,
                               error_messages={'required': 'Укажите логин'})
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                               min_length=3, max_length=50,
                               error_messages={'required': 'Укажите пароль'})
    class Meta:
        model = User
        fields = ('username', 'password')
