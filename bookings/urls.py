from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book-appointment', views.set_appointment, name='set_appointment'),
    path('appointment/', views.appointment_list, name='appointment_list'),

]