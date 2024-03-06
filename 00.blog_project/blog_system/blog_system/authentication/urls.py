from django.urls import path

from blog_system.authentication.views import SignUpView, SignInView, SignOutView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('sign-out/', SignOutView.as_view(), name='sign_out'),
)

from .receivers import *