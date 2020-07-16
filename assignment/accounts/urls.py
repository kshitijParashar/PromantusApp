
from django.urls import path
from . models import User
from . serializers import UserSerializer
from . resource_api import ResourceAPIView 



urlpatterns = [
	path('api/registration/<int:pk>', ResourceAPIView.as_view(model=User,resource_serializer=UserSerializer)),
	
	]