from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('list/', views.account_list, name='account_list'),
    path('create/', views.account_create, name='account_create'),
    path('<int:pk>/edit', views.account_edit, name='account_edit'),
    path('<int:pk>/delete', views.account_delete, name='account_delete'),

]