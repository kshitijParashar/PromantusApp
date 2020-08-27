
from django.urls import path
from authapp.views import RegisterView, LoginView, LogoutView
from accounts.views import Userdetails
# from django.views.generic import TemplateView

# app_name='authapp'

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login/userinfo/<int:pk>', Userdetails.as_view(), name='userinfo'),
    # path('user/<int:1>', Userdetails.as_view(), name='userinfo')
    # path('logout/', TemplateView.as_view(template_name="authlogin/logout.html"))

]