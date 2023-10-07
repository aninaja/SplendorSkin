from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth_login/login.html'), name='login'),
    path('login/process_login', views.process_login, name='process_login'),
    path('logout', views.process_logout, name='process_logout'),
    path('list/', views.account_list, name='account_list'),
    path('create/', views.account_create, name='account_create'),

]