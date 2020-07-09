from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from time import time


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        """
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        # database start time
        db_start = time()
        print("database start time is {}".format(db_start))
        try:

            user_profile = UserProfile.objects.get(pk=pk)

        except UserProfile.DoesNotExist:
            return Response({'message': 'The User Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # database access time
        db_time = time() - db_start
        print("database access time is {}".format(db_time))

        # Serializer start time
        serializer_start = time()
        print("Serializer start time is {}".format(serializer_start))

        serializer = UserProfileSerializer(user_profile)
        data = serializer.data

        # Serializer access time
        serializer_time = time() - serializer_start
        print("serializer access time is {}".format(serializer_time))

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk, *args, **kwargs):
        """

        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """

        try:

            user_profile = UserProfile.objects.get(pk=pk)

        except UserProfile.DoesNotExist:
            return Response({'message': 'The User Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user_profile, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwrgs):
        """
        :param request:
        :return:
        """
        # need to check Flag : is_active=True
        user_profile = UserProfile.objects.get(pk=pk)
        user_profile.delete()

        return Response({'message': ' User Profile is deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
