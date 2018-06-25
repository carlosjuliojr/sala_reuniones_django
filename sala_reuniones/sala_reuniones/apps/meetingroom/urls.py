# # -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import MeetingRoomViewSet 
router = DefaultRouter()
router.register(r'meetingroom', MeetingRoomViewSet, 'meetingroom')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
