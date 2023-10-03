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
    path('treatment-area/list/', views.treatment_area_list, name='treatedarea_list'),
    path('treatment-area/create/', views.treatment_area_create, name='treatedarea_create'),
    path('treatment-area/<int:pk>/edit', views.treatment_area_edit, name='treatedarea_edit'),

    # price type
    path('price-type/list/', views.price_type_list, name='pricetype_list'),
    path('price-type/create/', views.price_type_create, name='pricetype_create'),
    path('price-type/<int:pk>/edit', views.price_type_edit, name='pricetype_edit'),

    # treatment
    path('treatment/list/', views.treatment_list, name='treatment_list'),
    path('treatment/create/', views.treatment_create, name='treatment_create'),
    path('treatment/<int:pk>/edit', views.treatment_edit, name='treatment_edit'),
]