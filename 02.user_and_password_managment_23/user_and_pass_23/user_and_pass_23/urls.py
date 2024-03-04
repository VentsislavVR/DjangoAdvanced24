
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_and_pass_23.web.urls')),
    path('auth/', include('user_and_pass_23.app_auth.urls')),

]
