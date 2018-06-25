# -*- coding: utf-8 -*-

from rest_framework import viewsets
from .serializers import StateSerializer
from .models import State
from rest_framework.permissions import IsAdminUser 


class StateViewSet(viewsets.ModelViewSet,):
   
    model = State
    serializer_class = StateSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return State.objects.all()