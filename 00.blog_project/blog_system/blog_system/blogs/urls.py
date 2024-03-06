from django.urls import path

from blog_system.blogs import views

urlpatterns = (
    path('', views.BlogsListView.as_view(), name='index'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_details'),
    path('<int:pk>/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_details'),
    path('create/', views.BlogsCreateView.as_view(), name='blog_create'),


)