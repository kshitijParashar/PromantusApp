from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
# from .models import User
# from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
# from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated



"""-----------------------------using mixin classes----------------------------"""

# class ResourceCreateAPIView(CreateModelMixin, GenericAPIView):

# 	'''
#     User create API, need to submit all`name`,'username',email and `password` fields
  
#     '''
# 	model = None
#     resource_serializer = None
#     # permission_classes=[IsAuthenticated]
#     queryset = self.model.objects.all()
#     serializer_class = self.resource_serializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class UserProfileUpdateView(GenericAPIView, UpdateModelMixin):
#     '''
#     User  update API, need to submit all`name`,'username',email and `password`
#     At the same time, or django will prevent to do update for field missing
#     '''
#     model = None
#     resource_serializer = None
#     queryset = self.model.objects.all()
#     serializer_class = self.resource_serializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class UserProfilePartialUpdateView(GenericAPIView, UpdateModelMixin):
#     '''
#     need to submit all`name`,'username',email and `password`  
#     '''
#     model = None
#     resource_serializer = None
#     queryset = self.model.objects.all()
#     serializer_class = self.resource_serializer

#     def put(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

"""-----------------------------------mixin classes over here--------------------------------"""

class ResourceCreateAPIView(generics.CreateAPIView):
	"""	Used for create-only endpoints.
		Provides a post method handler."""
    model = None
    permission_classes = [permissions.AllowAny, IsAuthenticated]
    resource_serializer = None


class ResourceDetailView(generics.RetrieveAPIView):
	"""	Used for read-only endpoints to represent a single model instance.
		Provides a get method handler."""
	model = None
    queryset = self.model.objects.all()
    resource_serializer = None


class ResourceUpdateView(generics.RetrieveUpdateAPIView):
	"""	Used for update-only endpoints for a single model instance.
		Provides put and patch method handlers."""
	model = None
    queryset = self.model.objects.all()
    resource_serializer = None


class ResourceListView(generics.ListAPIView):
	"""	Used for read-write endpoints to represent a collection of model instances.
		Provides get and post method handlers."""
	model=None
    queryset = self.model.objects.all()
    resource_serializer = None


class ResourceDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
	"""	Used for delete-only endpoints for a single model instance.
		Provides a delete method handler.
		.destroy(request, *args, **kwargs) method, that implements deletion of an existing model instance.
		If an object is deleted this returns a 204 No Content response, otherwise it will return a 404 Not Found."""
	model=None
    queryset = self.model.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

"""------------------------------------GenericAPIView ends here-------------------------"""

#     def create(self, request, *args, **kwargs):

#         serializer = self.resource_serializer(data=request.data)
#         if (serializer.is_valid(raise_exception=True)):
#         	serializer.save()
#        		# headers = self.get_success_headers(serializer.data)
#         # token, created = Token.objects.get_or_create(user=serializer.instance)
			# return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=serializer.data)
#         	return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#     def retrieve(self, request, pk, *args, **kwargs):

#         try:
#             resource_item = self.model.objects.get(pk=pk)
#         #
#         except model.DoesNotExist:
#             return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.resource_serializer(resource_item)

#         return Response(serializer.data, status=status.HTTP_200_OK)
#     