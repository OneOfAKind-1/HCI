from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_info, name='service_info'),
]