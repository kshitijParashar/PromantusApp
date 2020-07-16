
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ResourceAPIView(APIView):
    permission_classes = []
    model = None
    resource_serializer = None

    def get(self, request, pk, *args, **kwargs):
        """
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            resource_item = self.model.objects.get(pk=pk)
        #
        except model.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.resource_serializer(resource_item)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk, *args,**kwargs):

        try:
            resource_item= self.model.objects.get(pk=pk)

        except model.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.resource_serializer(resource_item, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, pk, *args, **kwargs):
        """

        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
                
            #return Response(request.data['name'],status=status.HTTP_200_OK)

        serializer = self.resource_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

     
    
    def put(self, request, pk, *args, **kwargs):
        """

        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            resource_item= self.model.objects.get(pk=pk)

        except model.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.resource_serializer(resource_item, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        """
        :param request:
        :return:
        """
        # need to check Flag : is_active=True
        try:
            resource_item = self.model.objects.get(pk=pk)
        except model.DoesNotExist:
                return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)
        resource_item.delete()

        return Response({'message': 'The resource is deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
