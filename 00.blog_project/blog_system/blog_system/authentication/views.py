from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from blog_system.authentication.forms import SignUpForm, SignInForm


# Create your views here.
class SignUpView(views.CreateView):
    template_name = 'auth/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request,user)
        return valid

class SignInView(auth_views.LoginView):
    template_name = 'auth/signin.html'
    form_class = SignInForm

class SignOutView(auth_views.LogoutView):
    http_method_names = ['post', 'options', 'get']
    template_name = 'auth/signout.html'
    next_page = reverse_lazy('index')
