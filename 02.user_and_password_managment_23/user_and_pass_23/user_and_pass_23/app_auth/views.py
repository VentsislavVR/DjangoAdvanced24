from django import forms
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password,please."),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].help_text = 'It works'


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result
    # def get_success_url(self):
    #     pass
    # def get_form_class(self):
    #     if condition1:
    #         return condition1Form
    #     elif condition2:
    #         return condition2Form
    #     else:
    #         return condition3Form

class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


UserModel = get_user_model()

class ViewWithPermission(auth_mixins.PermissionRequiredMixin,views.TemplateView):
    template_name = 'app_auth/users_list.html'
class UsersListView(auth_mixins.LoginRequiredMixin,views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'

    # login_url = custom-login/url
