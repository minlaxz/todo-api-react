from django.urls import path, include

from rest_framework import urlpatterns
from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',TodoViewSet, basename='todos')

urlpatterns = [
    path('todos/', include(router.urls))
]