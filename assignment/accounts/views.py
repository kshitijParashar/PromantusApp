# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views.generic import View, UpdateView
from django.contrib import messages
# from .serializers import UserSerializer
from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import smtplib 
from django.contrib import sessions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from accounts.serializers import UserSerializer


#------------API fot testing---------------

class Userdetails(APIView):
	authentication_classes= [TokenAuthentication, SessionAuthentication, BasicAuthentication]

	def get(self, request, pk):
		queryset=User.objects.get(id=pk)
		serializer=UserSerializer(queryset)
		return Response(serializer.data, status=status.HTTP_200_OK)



"""------------------------------------For User registeration and  activatation----------------"""

class ActivateAccount(View):
	"""User Activation account"""
	# authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
	def get(self, request, uidb64, token, *args, **kwargs):
		try:
			uid = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=uid)
		except (TypeError, ValueError, OverflowError, User.DoesNotExist):
			user = None
		# if request.session['user']==user			
		if user is not None and account_activation_token.check_token(user, token):
			user.is_active = True
			user.is_staff = True
			user.profile.email_confirmed = True
			user.save()
			request.session.flush()
			login(request, user)
			return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
			# messages.sucess(request, ('Thank you for your email confirmation. Now you can login your account.'))
	
		else:
			# del request.session['user']
			 return HttpResponse('The confirmation link was invalid, possibly because it has already been used.')


class SignUpView(View):
	"""SignUp View"""
	# serializer_class=UserSerializer
	# authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
	form_class = None
	template_name = None

	def get(self, request, *args, **kwargs):
		# serializer=self.serializer_class(User.objects.all())
		form = self.form_class()
		return render(request, self.template_name, {'form': form})
		# return Response(serializer.data)
	# @csrf_exempt
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		# print(form)
		if form.is_valid(): # check form is valid or not if valid save it.
			user = form.save(commit=False)
			user.is_active = False # deactivate the user
			user.save()
			# print('hello')
			mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
			current_site = get_current_site(request)
			mail_subject = 'Activate your account.'

			message = render_to_string('accounts/account_activation_email.html', {
																					'user': user,
																					'domain': current_site.domain,
																					'uid':urlsafe_base64_encode(force_bytes(user.pk)),
																					'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			# print('hello2')
			
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			# send_mail(
			# 		    subject=mail_subject,
			# 		    message=message,
			# 		    from_email='test.promantus@gmail.com',
			# 		    recipient_list=[to_email],
			# 		    fail_silently=False,
			# 		)

			message = 'Subject: {}\n\n{}'.format(mail_subject, message)
			mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
			mailServer.starttls()

			mailServer.login('test.promantus@gmail.com' , 'kshitij@123')
			mailServer.sendmail('test.promantus@gmail.com', [to_email] , message)
			mailServer.login('from_your@gmail.com' ,'*********')
			mailServer.sendmail('from_your@gmail.com', [to_email] , message)
			print(" \n Sent!")
			mailServer.quit()
			# email.send()
			return render(request, 'accounts/home.html')
		return render(request, self.template_name, {'form': form})



def home(request):
	return render(request, 'accounts/home.html')

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response


"""---------------Session Login with authtoken------------------"""

from rest_framework.views import APIView
from accounts.serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class LoginView(APIView):
	# permission_classes=[IsAuthenticated,AllowAny]
	serializer_class = LoginSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data["user"]
		django_login(request, user) # ----------session Login 
		token, created = Token.objects.get_or_create(user=user)
		return Response({"token": token.key}, status=200)


class LogoutView(APIView):
	# permission_classes=[IsAuthenticated,AllowAny]
	authentication_classes = (SessionAuthentication , TokenAuthentication, )
	def post(self, request):
		django_logout(request) #--------Session Logout
		return Response(status=204)
		