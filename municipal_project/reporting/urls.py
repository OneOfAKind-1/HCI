from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_issue, name='report_issue'),
    path('home/', views.home, name='home'),          # <-- add this
    path('confirmation/', views.confirmation, name='confirmation'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
]