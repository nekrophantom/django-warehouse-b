from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutAdmin, name="logout"),

    path('home/', views.homePage, name="home"),
    path('dashboard/', views.dashboardPage, name="dashboard"),

    path('category-warehouse/', views.categoryWarehousePage, name="category-warehouse"),
    path('create-category-warehouse/', views.createCategoryWarehousePage, name="create-category-warehouse"),
    path('update-category-warehouse/<str:pk>/', views.updateCategoryWarehousePage, name="update-category-warehouse"),
    path('delete-category-warehouse/<str:pk>/', views.deleteCategoryWarehousePage, name="delete-category-warehouse"),
]
