"""instamojodemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from orders import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.home_view, name='home'),
     path('order/<uuid:product_id>/', views.order_page, name='order'),
     path('order-success/', views.order_success, name='order-success'),
     # path('get_instamojo_access_token/', views.get_instamojo_access_token, name='get_instamojo_access_token'),
     # path('create_payment_request/', views.create_payment_request, name='create_payment_request'),
]
