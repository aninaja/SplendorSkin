from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    # services
    path('list/', views.service_list, name='service_list'),
    path('create/', views.service_create, name='service_create'),
    path('<int:pk>/edit', views.service_edit, name='service_edit'),
    path('<int:pk>/delete', views.service_delete, name='service_delete'),

    # treatment area
    path('treatment-area/list/', views.treatment_area_list, name='treatment_area_list'),
    path('treatment-area/create/', views.treatment_area_create, name='treatment_area_create'),
    path('treatment-area/<int:pk>/edit', views.treatment_area_edit, name='treatment_area_edit'),
    path('<int:pk>/delete', views.treatment_area_delete, name='treatment_area_delete'),

    # price type
    path('price-type/list/', views.price_type_list, name='price_type_list'),
    path('price-type/create/', views.price_type_create, name='price_type_create'),
    path('price-type/<int:pk>/edit', views.price_type_edit, name='price_type_edit'),
    path('<int:pk>/delete', views.price_type_delete, name='price_type_delete'),

    # treatment
    path('treatment/list/', views.treatment_list, name='treatment_list'),
    path('treatment/create/', views.treatment_create, name='treatment_create'),
    path('treatment/<int:pk>/edit', views.treatment_edit, name='treatment_edit'),
    path('<int:pk>/delete', views.treatment_delete, name='treatment_delete'),
]