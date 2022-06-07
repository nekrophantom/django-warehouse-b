from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),

    path('home/', views.homePage, name="home"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
]
