from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('category-warehouse/', views.getCategoryWarehouse),
    # path('rooms/<str:pk>/', views.getRoom),
    
]