from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), 
    path('register/', views.signup, name = 'register'),
    path('login/', views.login, name = 'login'),
    # path('doubt//<int:pk>/', views.doubt, name = 'doubt'),
    path('stud_profile/<int:pk>/', views.stud_profile, name='stud_profile'),
    path('teacher_profile/<int:pk>/', views.teacher_profile, name='teacher_profile'),
]