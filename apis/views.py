# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
from todos import models
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = models.Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer