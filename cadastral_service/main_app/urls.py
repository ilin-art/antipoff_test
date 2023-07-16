from django.urls import path
from main_app import views


app_name = 'main_app'

urlpatterns = [
    path('query/', views.query_view, name='query'),
    path('result/', views.result_view, name='result'),
    path('ping/', views.ping_view, name='ping'),
]
