from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import EmailInput, PasswordInput
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '이메일을 입력 해주세요.',
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 입력 해주세요.',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 한번 더 입력 해주세요.',
            }),
        }