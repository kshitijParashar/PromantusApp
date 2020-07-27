
from django.urls import path
from . models import User
from . serializers import UserSerializer
from . resource_api import ResourceAPIView
from .generic_resource_api import * 
from .views import SignUpView, ActivateAccount, home,cookie_session, cookie_delete
from .forms import SignupForm



urlpatterns = [

# ----------------for simple registration----------------------------------

	path('api/registration/<int:pk>', ResourceAPIView.as_view(model=User,resource_serializer=UserSerializer)),
	path('api/POST/registration/', ResourceCreateAPIView.as_view()),
	path('api/GET/registration/<int:pk>', ResourceDetailView.as_view()),
	path('api/PUT/registration/<int:pk>', ResourceUpdateView.as_view()),
	path('api/GET/POST/registration/<int:pk>', ResourceListView.as_view()),
	# path('api/DELETE/registration/<int:pk>', ResourceDeleteView.as_view()),

	#-------------for signup with email verification link--------------------
	
    path('signup/', SignUpView.as_view(form_class=SignupForm, template_name='accounts/signup.html'), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('home/', home, name='home'),


    # --------------------for testing cookies and session only----------------
#     path('testcookie/', cookie_session),
#     path('deletecookie/', cookie_delete),
]
	
	