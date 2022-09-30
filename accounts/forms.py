from django import forms
from .models import SiteUser


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())

    class Meta:
        model = SiteUser
        fields = ('username', 'first_name', 'last_name', 'email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']


class LoginForm(forms.Form):
    email = forms.CharField(label='Адрес электронной почты', widget=forms.EmailInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not SiteUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Такого пользователя не существует')
        user = SiteUser.objects.filter(email=email).first()
        if not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data
