from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# from .filterset import UserProfileFilter
# from django_filters import rest_framework as filters
from time import time
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import mixins
from urllib import parse


class UserProfileListView(APIView):
    permission_classes = []
    model = UserProfile
    resource_serializer = UserProfileSerializer

    def get(self, request, field_name, field_value, *args, **kwargs):
        """
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        # self.filter_data = dict()
        try:
            print(request)
            self.filter_query(request)
            print(self.filter_query(request))
            self.filter_data[field_name] = field_value
            print(self.filter_data)
            resource_item_list = self.model.objects.filter(data__contains= self.filter_data)
            print(resource_item_list)



        except self.model.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # raise ValueError(resource_item_list.__dict__)
        serializer = self.resource_serializer(resource_item_list)
        print(serializer)
        print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)



    def filter_query(self, request):
        self.filter_data = dict()
        kwargs={self.kwargs.get('field_name') : self.kwargs.get('field_value')}
        print(kwargs)
        for k, v in kwargs:
            if k.endswith('__contains'):
                self.filter_data[k] = request.query_params.get(k)
                continue
            self.filter_data[k] = v

# {'{0}__{1}'.format('data', self.kwargs.get('field_name')): self.kwargs.get('field_value')}
#
#
# class UserProfileListView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     # serializer_class = UserProfileSerializer
#     model=UserProfile
# #     # allowed_methods = ['GET']
# #     queryset = UserProfile.objects.all()
# #     filter_backends = [UserProfileFilter,]
# #     filter_fields = ['data']
# #
#     def get_queryset(self):
#         qs = self.model.objects.all()
#         print(qs)
#         product_filtered_list=UserProfileFilter(self.request.GET,queryset=qs)
#         print(product_filtered_list)
#         print(product_filtered_list.qs)

        # serializer = UserProfileSerializer(queryset, many=True)
        # return product_filtered_list.qs

        # return UserProfile.objects.filter(data=field_value)


    # def get_queryset(self):
    #     queryset = UserProfile.objects.all()
    #     field_name = self.request.query_params.get('field_name', None)
    #     if field_name is not None:
    #         queryset = queryset.filter(data=self.kwargs["data"])
    #     return queryset


"""-----------------Static APIView Filtering for Json Field-----------------------"""

    # def get(self, request, field_name, field_value, *args, **kwargs):
    #     """
    #     :param request:
    #     :param pk:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     # checking using age fields
    #     if field_name == "age":
    #
    #         try:
    #             resource_item_list = UserProfile.objects.filter(data__age__gte=int(field_value))
    #             # print(resource_item_list)
    #         except UserProfile.DoesNotExist:
    #             return Response({'message': 'The User Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #
    #         serializer = UserProfileSerializer(resource_item_list, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #     # checking using address fields
    #
    #     elif field_name == "address":
    #
    #         try:
    #             resource_item_list = UserProfile.objects.filter(data__address=field_value)
    #             # print(resource_item_list)
    #         except UserProfile.DoesNotExist:
    #             return Response({'message': 'The User Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #
    #         serializer = UserProfileSerializer(resource_item_list, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)





"""-----------------Dynamic APIView Filtering for Json Field-----------------------"""

# class UserProfileListView(APIView):
#         def get(self, request, field_name, field_value, *args, **kwargs):
#             """
#             :param request:
#             :param pk:
#             :param args:
#             :param kwargs:
#             :return:
#             """
#             # checking using age fields
#
#             print({field_name:field_value})
#             try:
#                 resource_item_list = UserProfile.objects.filter(data__contains={f"{field_name}":field_value})
#                 print(resource_item_list)
#             except UserProfile.DoesNotExist:
#                 return Response({'message': 'The User Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#             serializer = UserProfileSerializer(resource_item_list, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)

"""---------------------Generic ListAPIView---------------------------"""
# class UserProfileListView(ListCreateAPIView):
#         model= UserProfile
#         serializer_class = UserProfileSerializer


#         """Override the get_queryset"""

#         def get_queryset(self):
#             """
#             field_name
#             field_value
#             :return:
#             """
#             # query_data=dict()
#             # query_fields=self.kwargs
#             # print(query_fields)

            
#             #     kwargs = {'{0}__{1}'.format('data', self.kwargs.get('field_name')): self.kwargs.get('field_value')}
#             #     return UserProfile.objects.filter(**kwargs)
        
#             field_name = self.kwargs["field_name"]
#             field_value = self.kwargs["field_value"]
        
#             """return Filter the queryset"""
        
#             return self.model.objects.filter(data__contains={f"{field_name}":int(field_value) })
            # return UserProfile.objects.filter(**query_fields)


        # def get_queryset(self):
        #     queryset = UserProfile.objects.all()
        #     print(queryset)
        #     field_name = self.request.query_params.get('field_name',None)
        #     print(field_name)
        #     if field_name is not None:
        #         queryset = queryset.filter(userprofile__contains=field_name)
        #         print(queryset)
        # #     return queryset


# # 
# class UserProfileListView(ListAPIView):
#         model= UserProfile
#         serializer_class = UserProfileSerializer

#         def get_queryset(self):
#             queryset = UserProfile.objects.all()
#             print(queryset)
#             field_name = self.request.GET.get('field_name')
#             print(field_name)
#             if field_name is not None:
#                 queryset = queryset.filter(data__contains=field_name)
#                 print(queryset)
# #                 return queryset
        
# class UserProfileListView(ListCreateAPIView, mixins.RetrieveModelMixin):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     lookup_field = 'field_name'
#     
#     def retrieve(self, request, *args, **kwargs ):
#         field_name=kwargs.get('field_name', None)
#         data=data.objects.get(field_name)
#         self.queryset=
        
        
        