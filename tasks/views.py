from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import mixins


from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from .permissions import IsAdminOrOwner


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('owner').all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all().order_by('-created_at')
        return Task.objects.filter(owner=user).order_by('-created_at')


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsAdminOrOwner])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.status = True
        task.save()
        return Response(self.get_serializer(task).data)


    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsAdminOrOwner])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = False
        task.save()
        return Response(self.get_serializer(task).data)