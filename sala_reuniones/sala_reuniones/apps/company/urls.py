# # -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet 

#routers
router = DefaultRouter()
router.register(r'company', CompanyViewSet, 'company')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
