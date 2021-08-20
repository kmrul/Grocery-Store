from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.apiOverview, name='customer-apioverview'),
    path('customer/list/', views.customerList, name='customer-list'),
    path('customer/detail/<str:pk>', views.customerDetail, name='customer-detail'),
    path('customer/create', views.customerCreate, name='customer-create'),
    path('customer/update/<str:pk>', views.customerUpdate, name='customer-update'),
    path('customer/delete/<str:pk>', views.customerDelete, name='customer-delete'),
]