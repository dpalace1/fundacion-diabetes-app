from django.urls import path
from . import views

urlpatterns = [
    path('donation/', views.donation, name="blog-donations"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]