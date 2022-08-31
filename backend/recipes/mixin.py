from rest_framework import mixins
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response


# class AddDelViewMixin:

#     def add_del_obj(self, obj_id, manager):
#         user = self.request.user
#         if user.is_anonymous:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)

#         MANAGERS = {
#             'subscribe': user.subscription,
#             'favorite': user.favorites,
#             'shopping_cart': user.in_cart,
#         }

#         manager = MANAGERS[manager]
#         obj = get_object_or_404(self.queryset, id=obj_id)
#         serializer = self.add_serializer(
#             obj,
#             context={'request': self.request}
#         )
#         exists = manager.filter(id=obj_id).exists()

#         if not exists and self.request.method in ('GET', 'POST'):
#             manager.add(obj)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         if exists and self.request.method in ('DELETE',):
#             manager.remove(obj)
#             return Response(status=status.HTTP_204_NO_CONTENT)



