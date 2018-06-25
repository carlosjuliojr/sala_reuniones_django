# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company


class CompanyViewSet(viewsets.ModelViewSet,):
   
    model = Company
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()