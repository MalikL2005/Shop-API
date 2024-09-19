from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-up/validate/', views.validate_sign_up, name='validate_sign-up'),
]