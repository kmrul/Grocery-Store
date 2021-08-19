from django.urls import path
from . import views

urlpatterns = [
    path('category', views.apiOverview, name='overview'),
    path('category/list/', views.categorylist, name='category-list'),
    path('category/detail/<str:pk>', views.categoryDetail, name='category-detail'),
    path('category/create', views.categoryCreate, name='category-create'),
    path('category/update/<str:pk>', views.categoryUpdate, name='category-update'),
    path('category/delete/<str:pk>', views.categoryDelete, name='category-delete'),
]