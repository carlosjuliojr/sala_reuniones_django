# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .serializers import SupplySerializer
from .models import Supply


class SupplyViewSet(viewsets.ModelViewSet,):
   
    model = Supply
    serializer_class = SupplySerializer


    def get_queryset(self):
        return Supply.objects.all()
