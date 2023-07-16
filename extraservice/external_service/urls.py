from django.urls import path
from external_service import views


app_name = 'external_service'

urlpatterns = [
    path('', views.process_request, name='process'),
]