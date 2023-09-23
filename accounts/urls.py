from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
                  path('create/', views.account_create, name='account_create'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
