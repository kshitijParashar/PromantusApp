
from django.urls import path

from accounts.models import User
from accounts.serializers import UserSerializer
from accounts.apis.resource_api import ResourceAPIView
from accounts.apis.generic_resource_api import * 
# from accounts.views import SignUpView, ActivateAccount

from accounts.models import User
from accounts.serializers import UserSerializer #LoginSerializer
from accounts.apis.resource_api import ResourceAPIView
from accounts.apis.generic_resource_api import * 
from accounts.views import (
	SignUpView, 
	ActivateAccount, 
	home,
	cookie_session, 
	cookie_delete,
	# LoginView,
	# LogoutView,
	Userdetails
	)

from accounts.forms import SignupForm



urlpatterns = [

# ----------------for simple registration----------------------------------

	# path('api/registration/<int:pk>', ResourceAPIView.as_view(model=User,resource_serializer=UserSerializer)),
	# path('api/POST/registration/', ResourceCreateAPIView.as_view()),
	# path('api/GET/registration/<int:pk>', ResourceDetailView.as_view()),
	# path('api/PUT/registration/<int:pk>', ResourceUpdateView.as_view()),
	# path('api/GET/POST/registration/<int:pk>', ResourceListView.as_view()),
	# path('api/DELETE/registration/<int:pk>', ResourceDeleteView.as_view()),

	#-------------for signup with email verification link--------------------
	
    path('signup/', SignUpView.as_view(form_class=SignupForm, template_name='accounts/signup.html'), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('home/', home, name='home'),

#   -----------for api testing on authentication---------------------
    path('user/<int:pk>', Userdetails.as_view(), name="userinfo")

    # --------------------for testing cookies and session only----------------
#     path('testcookie/', cookie_session),
#     path('deletecookie/', cookie_delete),
]
	
	