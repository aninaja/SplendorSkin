from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('list/', views.account_list, name='account_list'),
    path('create/', views.account_create, name='account_create'),

]