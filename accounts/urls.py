"""django_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('products/', views.products, name= 'products'),
    path('customer/<int:pk>/', views.customer, name = 'customer'),
    path('user/', views.userPage, name= 'user_page'),
    path('account/', views.accountSettings, name= 'account'),


    path('register/', views.registerPage, name= 'register'),
    path('login/', views.loginPage, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),

    path('order_form/<int:pk>/', views.createOrder, name = 'order_form' ),
    path('update_form/<int:pk>/', views.updateOrder, name = 'update_order' ),
    path('delete_order/<int:pk>/', views.deleteOrder, name = 'delete_order' ),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name = 'reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]
