from rest_framework import serializers
# from .models import User
from django.contrib.auth.models import User
from accounts.models import Profile



class UserSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    first_name=serializers.CharField(max_length=30, required=False, help_text='Optional')
    last_name=serializers.CharField(max_length=30, required=False, help_text='Optional')
    email = serializers.EmailField(required=False)
    class Meta:
        model = User
        # # fields = ('first_name',
        #         'last_name',
        #         'email',
        #         'id',
        #         'phone',
                # )
        fields = [
                'id',
                'username', 
                'first_name', 
                'last_name', 
                'email', 
                # 'password1', 
                # 'password2', 
            ]

        read_only_fields = ('id',)


    def create(self, validated_data):
        # import secrets
        # import string
        # alphabet = string.ascii_letters + string.digits
        # password = ''.join(secrets.choice(alphabet) for i in range(20))
        try:
            user_exist = User.objects.get(email=validated_data["email"])
        except:
            user_exist = None
        if user_exist == None:
            user = User.objects.create(
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name = validated_data["last_name"],
                phone = validated_data["phone"],
                )
            user.set_password(password)
            user.save()
            return user
        else:
            #updating user credentials in case user exists
            #if we are updating the username in case it exists globally
            keys_to_update = ['first_name','last_name', 'phone']
            for val in keys_to_update:
                setattr(user_exist,val,validated_data[val])
            user_exist.save() 
            return user_exist



    def update(self, instance, validated_data):
        return super().update(instance,validated_data)

# class ProfileSerializer(serializers.ModelSerializer):

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('username', 'email', 'is_active', 'is_staff')
"""---------------------------Login Serializer-------------------------------------"""

from django.contrib.auth import authenticate
from rest_framework import exceptions


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data

