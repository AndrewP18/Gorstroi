from rest_framework import generics
from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
