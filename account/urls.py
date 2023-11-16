from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    #Pagine Statiche
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    #Login e Registrazione utente
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
