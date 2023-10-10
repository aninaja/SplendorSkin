from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book-appointment', views.appointment_set, name='appointment_set'),
    path('appointment/', views.appointment_list, name='appointment_list'),

]