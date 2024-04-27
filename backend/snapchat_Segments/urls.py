
from django.urls import path
from . import views

urlpatterns = [
    path('customer_lists/', views.customer_list_list, name='customer_list_list'),
    path('customer_lists/<int:pk>/', views.customer_list_detail, name='customer_list_detail'),
    path('snapchat_oauth/', views.start_oauth, name='snapchat_oauth'),
    path('callback/', views.SnapchatCallbackView.as_view(), name='snapchat_callback'),

]