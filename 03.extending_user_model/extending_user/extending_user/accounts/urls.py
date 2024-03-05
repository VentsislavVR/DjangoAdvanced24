from django.urls import path

from extending_user.accounts.views import LoginUserView

urlpatterns = (

    path('login/', LoginUserView.as_view(), name='login_user'),
    # path('register/', RegisterUserView.as_view(), name='register'),

)