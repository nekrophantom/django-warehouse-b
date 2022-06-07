from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutAdmin, name="logout"),

    path('home/', views.homePage, name="home"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('category-warehouse/', views.categoryWarehousePage, name="category-warehouse"),
]
