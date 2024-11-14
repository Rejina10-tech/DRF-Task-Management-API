from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Task.objects.none()  
        
        if self.request.user.is_superuser:
            return Task.objects.all()  
        
        return Task.objects.filter(owner=self.request.user)  
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    