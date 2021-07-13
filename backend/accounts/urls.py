from django.urls import path
from .views import ListUser, DetailUser, UpdateUser, address, edit_address

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', ListUser.as_view(), name='user'),
    path('user/<int:pk>/', DetailUser.as_view(), name='user-details'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update-details'),
    path('address/', address, name='address'),
    path('edit_address/<int:pk>/', edit_address, name='edit-address'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
