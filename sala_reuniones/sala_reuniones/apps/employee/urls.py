# # -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import  UserViewSet, UsersViewSet

router = DefaultRouter()
router.register(r'register', UserViewSet , 'register')
router.register(r'users', UsersViewSet , 'users')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    # url(r'^$api/v1/user/', UserViewSet.as_view()),
]
