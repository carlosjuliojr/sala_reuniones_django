# # -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BookMeetingRoomViewSet 
router = DefaultRouter()
router.register(r'bookmeetingroom', BookMeetingRoomViewSet, 'bookmeetingroom')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
