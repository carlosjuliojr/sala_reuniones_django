# # -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import StateViewSet 
router = DefaultRouter()
router.register(r'state', StateViewSet, 'state')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
