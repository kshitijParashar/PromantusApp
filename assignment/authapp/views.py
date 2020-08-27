
from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework_api_key.models import APIKey
import datetime
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout
from authapp.backends import JWTAuthentication
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from django.views.generic import TemplateView
# from rest_framework.renderers import TemplateHTMLRenderer



# from Crypto.PublicKey import RSA
# Create your views here.



# JWT_SECRET_KEY = "JWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEY"

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(GenericAPIView, TemplateView):
    serializer_class = LoginSerializer
    template_name = "authlogin/login.html"
    # renderer_classes = [TemplateHTMLRenderer]
    print(serializer_class)
    permission_classes=(AllowAny,)
# 
    def post(self, request):
        data = request.data
        print("1-->",data)
        username = data.get('username', '')
        password = data.get('password', '')
        print("2-->", username)
        print("3-->",password)
        user = auth.authenticate(username=username, password=password)
        print("4-->", user)
        django_login(request, user) # ----------session Login
        session_id=request.session.session_key
        print ("sessionid Login:",session_id)
        print("6-->", session_id)
        if user:
            auth_token = jwt.encode(
	                		
	                	payload = {
				        			"iss": "Kshitij",                 # String - The Provider ID found in the Layer Dashboard
				        			"prn": user.id,                   # String - Provider's internal ID for the authenticating user
				        			"iat": datetime.datetime.now(),   # Integer - Time of Token Issuance in RFC 3339 seconds
				        			"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=300),   # Integer - Arbitrary Token Expiration in RFC 3339 seconds
				        			"username": user.username,
                                    "sessionid":session_id,
	        						}, 
	        			key = settings.JWT_SECRET_KEY["private_key"],
	        			headers = {
				        			"typ": "JWS",               # String - Expresses a MIME Type of application/JWS
				        			"alg": "RS256",             # String - Expresses the type of algorithm used to sign the token, must be RS256
				        			"cty": "layer-eit;v=1",     # String - Express a Content Type of Layer External Identity Token, version 1
				        			"kid": "key-id-12345"       # String - Private Key associated with "layer.pem", found in the Layer Dashboard
	    						},
	        			algorithm='RS256')
            print(auth_token)
            serializer = self.serializer_class(user)
            # serializer.is_valid(raise_exception=True)
            # user = serializer.validated_data["user"]
            data = {'user': serializer.data, 'token': auth_token, 'sessionid':session_id}
            print("5-->", serializer.data)
            return Response(data, status=status.HTTP_200_OK)
            

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(GenericAPIView, TemplateView):
    permission_classes=[IsAuthenticated,AllowAny]
    template_name = "authlogin/logout.html"
    # renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = (SessionAuthentication )
    def post(self, request):
        django_logout(request) #--------Session Logout
        return Response({"msg": 'Logout successfully'}, status=status.HTTP_200_OK)