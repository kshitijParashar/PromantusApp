
from django.urls import path
from . models import User
from . serializers import UserSerializer
from . resource_api import ResourceAPIView
from .generic_resource_api import * 



urlpatterns = [
	path('api/registration/<int:pk>', ResourceAPIView.as_view(model=User,resource_serializer=UserSerializer)),
	path('api/POST/registration/', ResourceCreateAPIView.as_view()),
	path('api/GET/registration/<int:pk>', ResourceDetailView.as_view()),
	path('api/PUT/registration/<int:pk>', ResourceUpdateView.as_view()),
	path('api/GET/POST/registration/<int:pk>', ResourceListView.as_view()),
	# path('api/DELETE/registration/<int:pk>', ResourceDeleteView.as_view()),

	
	]