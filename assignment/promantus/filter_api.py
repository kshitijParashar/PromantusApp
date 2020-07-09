from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from django_filters import rest_framework as filters
from time import time
from rest_framework import generics


class UserProfileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, field_name, field_value, *args, **kwargs):
        """
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        # checking using age fields
        if field_name == "age":

            try:
                resource_item_list = UserProfile.objects.filter(data__age__gte=int(field_value))
                # print(resource_item_list)
            except UserProfile.DoesNotExist:
                return Response({'message': 'The User Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

            serializer = UserProfileSerializer(resource_item_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # checking using address fields

        elif field_name == "address":

            try:
                resource_item_list = UserProfile.objects.filter(data__address=field_value)
                # print(resource_item_list)
            except UserProfile.DoesNotExist:
                return Response({'message': 'The User Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

            serializer = UserProfileSerializer(resource_item_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
