# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import BookMeetingRoomSerializer
from .models import BookMeetingRoom
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class BookMeetingRoomViewSet(viewsets.ModelViewSet,):
   
    model = BookMeetingRoom
    serializer_class = BookMeetingRoomSerializer
    permission_classes = IsAdminUser,

    def get_queryset(self):
        return BookMeetingRoom.objects.all()

