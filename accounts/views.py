from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy  # reverse для FBV, reverse_lazy для CBV
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import SiteUser
from .forms import RegisterForm, LoginForm


# Create your views here.


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        data = {'form': form}
        return render(request, 'accounts/register.html', data)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return HttpResponseRedirect(reverse_lazy('login'))
        data = {'form': form}
        return render(request, 'accounts/register.html', data)


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        data = {'form': form}
        return render(request, 'accounts/login.html', data)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        data = {'form': form}
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'accounts/login.html', data)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class UserView(View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(SiteUser, username=kwargs.get('username'))
        data = {'user': user}
        return render(request, 'accounts/user_profile', data)
