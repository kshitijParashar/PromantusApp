# import django_filters
# from .models import UserProfile
# # from django.db import models
# #
# #
# #
# #
# class UserProfileFilter(django_filters.rest_framework.FilterSet):
#     name = django_filters.CharFilter(field_name="name", lookup_expr='exact')
#     age__gte=django_filters.NumberFilter(field_name='data__age', lookup_expr='gte')
#     age__lte=django_filters.NumberFilter(field_name ='data__age', lookup_expr='lte')
#     address=django_filters.CharFilter(field_name="data__address",lookup_expr='exact')
#
#     class Meta:
#         model = UserProfile
#         # fields = ('name','age__gte', 'age__lte', 'address')
#         fields = ['name','data']
#         # filter_overrides = {
#         #     models.CharField: {
#         #         'filter_class': django_filters.NumberFilter,
#         #         'extra': lambda f: {
#         #             'lookup_expr': 'icontains',
#         #         }
