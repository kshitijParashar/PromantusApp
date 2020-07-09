from django.urls import path, include
from .views import UserProfileView
from .filter_api import UserProfileListView

urlpatterns = [
    path('api/userprofile/<int:pk>', UserProfileView.as_view()),
    path('api/userprofile/<str:field_name>/<str:field_value>', UserProfileListView.as_view())

]
