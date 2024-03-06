from django.contrib.auth import forms as auth_forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
# Create your views here.
class SignUpView(views.CreateView):
    template_name = 'auth/signup.html'
    form_class = auth_forms.UserCreationForm
    success_url = reverse_lazy('index')

class SignInView(auth_views.LoginView):
    template_name = 'auth/signin.html'

class SignOutView(auth_views.LogoutView):
    http_method_names = ['post', 'options', 'get']
    template_name = 'auth/signout.html'
    next_page = reverse_lazy('index')
