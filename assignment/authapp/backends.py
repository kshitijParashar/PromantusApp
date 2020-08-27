
import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User

# JWT_SECRET_KEY = "JWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEY"

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        print(request)
        auth_data = authentication.get_authorization_header(request)
        print(auth_data)
        print('hello')
        print(request.session.session_key)
        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY["public_key"], algorithm='RS256')
            print(payload)
            print(request.session.session_key)
            
            try:

                if payload.get('sessionid')== request.session.session_key:
                    user = User.objects.get(username=payload['username'])
                    return (user, token)
                else:
                    return None

            except jwt.DecodeError as identifier:
                msg= 'You have not permission to access'
                raise exceptions.AuthenticationFailed(msg) 

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')

        return super().authenticate(request)


# class HasAPIKey():
#     pass