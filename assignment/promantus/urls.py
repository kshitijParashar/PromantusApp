from django.urls import path, include
from .views import UserProfileView
from .filter_api import UserProfileListView
from django.conf.urls import url

urlpatterns = [
    url('api/userprofile/<int:pk>', UserProfileView.as_view()),
    url('api/userprofile/<str:field_name>=<field_value>', UserProfileListView.as_view()),
    url('api/userprofile/<str:name>', UserProfileListView.as_view()),
    url('^api/userprofile/field_name/field_value $', UserProfileListView.as_view()),


]
