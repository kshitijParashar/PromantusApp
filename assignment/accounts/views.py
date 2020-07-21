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

class ActivateAccount(View):
	"""User Activation account"""
	def get(self, request, uidb64, token, *args, **kwargs):
		try:
			uid = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=uid)
		except (TypeError, ValueError, OverflowError, User.DoesNotExist):
			user = None
		if user is not None and account_activation_token.check_token(user, token):
			user.is_active = True
			# user.is_staff = True
			user.profile.email_confirmed = True
			user.save()
			login(request, user)
			return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
			# messages.sucess(request, ('Thank you for your email confirmation. Now you can login your account.'))
	
		else:
			 return HttpResponse('The confirmation link was invalid, possibly because it has already been used.')


class SignUpView(View):
	"""SignUp View"""
	# serializer_class=UserSerializer
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
	
			email.send()
			return redirect('home')
		return render(request, self.template_name, {'form': form})
			
		
	


def home(request):
	return render(request, 'accounts/home.html')




