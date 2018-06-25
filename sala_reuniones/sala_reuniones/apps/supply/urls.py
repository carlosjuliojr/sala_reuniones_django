# # -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import SupplyViewSet 
router = DefaultRouter()
router.register(r'supply', SupplyViewSet, 'supply')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
