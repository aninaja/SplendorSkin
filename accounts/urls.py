from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('logout', views.process_logout, name='process_logout'),
    path('list/', views.account_list, name='account_list'),
    path('create/', views.account_create, name='account_create'),

]