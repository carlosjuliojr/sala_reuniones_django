# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, is_authenticated, IsAdminUser,)
from .serializers import UserSerializer
from django.contrib.auth.models import User



#Para que un empleado pueda registrarse en el sistema por eso es AllowAny
class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(email=user.username)

#Solo El administrador puede hacer CRUD sobre cualquier empleado
class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return User.objects.all()

