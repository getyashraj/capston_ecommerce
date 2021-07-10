from django.urls import path
from .views import ListUser, DetailUser, UpdateUser

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', ListUser.as_view(), name='user'),
    path('user/<int:pk>/', DetailUser.as_view(), name='user-details'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
