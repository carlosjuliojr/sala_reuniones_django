# -*- coding: utf-8 -*-

from rest_framework import viewsets
from .serializers import MeetingRoomSerializer
from .models import MeetingRoom
from rest_framework.permissions import IsAdminUser


class MeetingRoomViewSet(viewsets.ModelViewSet,):
   
    model = MeetingRoom
    serializer_class = MeetingRoomSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return MeetingRoom.objects.all()