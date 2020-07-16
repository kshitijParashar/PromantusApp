
from django.urls import path
from . models import User
from . serializers import UserSerializer
from . resource_api import ResourceAPIView
from .generic_resource_api import * 



urlpatterns = [
	path('api/registration/<int:pk>', ResourceAPIView.as_view(model=User,resource_serializer=UserSerializer)),
	path('api/POST/registration/<int:pk>', ResourceCreateAPIView.as_view(model=User,resource_serializer=UserSerializer)),
	
	]