from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import CustomUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# class User(AbstractUser):
#     """
#     Store a single user and inherits the AbstractUser class. This model will be responsible 
#     for the authentication process on the basis of email id and password.
    
#     """
#     username = models.CharField(max_length=100, blank=True, null=True)
#     # photo = models.ImageField(upload_to="user_image",null=True,blank=True)          
#     email = models.EmailField(unique=True, max_length=254)
#     phone=models.CharField(max_length=15, null=True,blank=True, unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()

#     def __str__(self):
#         return "{}".format(self.email)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()