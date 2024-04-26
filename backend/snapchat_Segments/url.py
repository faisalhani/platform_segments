
from django.urls import path
from . import views

urlpatterns = [
    path('customer_lists/', views.customer_list_list, name='customer_list_list'),
    path('customer_lists/<int:pk>/', views.customer_list_detail, name='customer_list_detail'),
    # Add URL patterns for other views as needed
]