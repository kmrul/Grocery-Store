from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.apiOverview, name='order-apioverview'),
    path('order/list', views.orderList, name='order-list'),
    path('order/create', views.orderCreate, name='order-create'),
    path('order/detail/<str:pk>', views.orderDetail, name='order-detail'),
    path('order/update/<str:pk>', views.orderUpdate, name='order-update'),
    path('order/delete/<str:pk>', views.orderDelete, name='order-delete'),
    path('orderline/list/<str:pk>', views.orderLineByOrder, name='order-line-by-order'),
    path('orderline/create', views.orderLineCreate, name='orderline-create'),
    path('orderline/update/<str:pk>', views.orderLineUpdate, name='orderline-update'),
    path('orderline/delete/<str:pk>', views.orderLineDelete, name='orderline-delete'),

]