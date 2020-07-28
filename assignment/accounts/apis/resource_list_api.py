from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ResourceListAPIView(APIView):
    permission_classes = []
    model = None
    resource_serializer = None

    def get(self, request, field_name, field_value,*args, **kwargs):
        """
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            self.filter_query(request)
            self.filter_data[field_name] = field_value
            resource_item_list = self.model.objects.filter(**self.filter_data)
        
        except self.model.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)
        #raise ValueError(resource_item_list.__dict__)
        serializer = self.resource_serializer(resource_item_list)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, field_name,field_value="", *args, **kwargs):
        """

        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        if field_name=="CREATE":
            serializer = self.resource_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        else:
            try:
                self.filter_query(request)
                self.filter_data[field_name] = field_value
                resource_item_list = self.model.objects.filter(**self.filter_data)
            except self.model.DoesNotExist:
                return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)

            serializer = self.resource_serializer(resource_item_list, data=request.data,read_only=False)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, field_name, field_value="" ,*args, **kwargs):
        """
        :param request:
        :return:
        """
        # need to check Flag : is_active=True
        try:
            field_dict = dict()
            field_dict[field_name] = field_value
            resource_item_list = self.model.objects.filter(data=**field_dict) 
        except self.model.DoesNotExist:
                return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)
        resource_item_list.delete()

        return Response({'message': 'The resource is deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    def filter_query(self,request):
        self.filter_data = dict()
        for k,v in request.query_params.items():
            if k.endswith('__in'):
                self.filter_data[k] = request.query_params.getlist(k)
                continue
            self.filter_data[k] = v


