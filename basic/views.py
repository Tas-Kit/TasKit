# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy

from forms import SignUpForm

# Create your views here.


class ResetPasswordView(PasswordResetView):
    email_template_name = 'basic/reset_password_email.html'
    success_url = reverse_lazy('basic:reset_password_done')
    template_name = 'basic/reset_password.html'


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'basic/reset_password_done.html'


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'basic/reset_password_confirm.html'
    success_url = reverse_lazy('basic:password_reset_complete')


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'basic/reset_password_complete.html'


class LoginView(TemplateView):
    template_name = 'basic/login.html'

    def get(self, request):
        form = AuthenticationForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('basic:home')
        args = {'form': form}
        return render(request, self.template_name, args)


class SignupView(TemplateView):
    template_name = 'basic/signup.html'

    def get(self, request):
        form = SignUpForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = SignUpForm(data=request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('basic:home')
        args = {'form': form}
        return render(request, self.template_name, args)


class HomeView(TemplateView):
    template_name = 'basic/home.html'
