from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), 
    path('register/', views.signup, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('stud_profile/<int:pk>/', views.stud_profile, name='stud_profile'),
    path('doubtlist/<int:pk>/', views.doubtlist, name='doubtlist'),
    path('tech_doubt/<int:pk>/', views.test1, name='tech_doubt'), 
    path('doubt/<int:pk>/', views.doubt, name='doubt'), 
    path('offered/<int:pk>/', views.test2, name='offered'), 
    path('payment/<int:pk>/', views.pay, name='payment'), 
    path('teacher_profile/<int:pk>/', views.teacher_profile, name='teacher_profile'),
    path('logout', views.logout, name = 'logout'),  
]