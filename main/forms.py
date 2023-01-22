from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddIncomeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['manufacturer'].empty_label = 'Новый производитель...'
        self.fields['manufacturer'].required = False

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': "Название товара"}),
            'category': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': "Категория"}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1',
                                              'placeholder': "Цена"}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': '1',
                                               'placeholder': "Кол-во"}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control',
                                                      'placeholder': "Срок годности"}),
            'image': forms.FileInput(attrs={'class': 'income_input form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10,
                                                 "style": "resize: vertical; height: 130px; max-height: 260px;",
                                                 'placeholder': "Описание"}),
            'manufacturer': forms.Select(attrs={'class': 'form-control', 'id': 'income_manufacturer'})
        }
