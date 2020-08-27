"""assignment URL Configuration

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
from django.contrib import admin
from django.urls import path, include
# from accounts.views import LoginView, LogoutView
# from rest_framework.permissions import IsAuthenticated, AllowAny
# permission_classes= (AllowAny,)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('promantus.urls')),
    path('api/accounts/',include('accounts.urls')),
    path('api/auth/',include('authapp.urls')),
    # path('api/accounts/auth/login',LoginView.as_view(), name='login'), # Session Login url
    # path('api/accounts/auth/logout',LogoutView.as_view(), name='logout'), #session Logout url
    
    # path('accounts/', include('rest_registration.api.urls')),
]
