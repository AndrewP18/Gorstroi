from rest_framework import generics
from django.shortcuts import render
from .models import Project, Image, Company_contact, Feedback_form
from .serializers import ProjectSerializer, ImageSerializer, Company_contactSerializer, Feedback_formSerializer


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ImageAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class Company_contactAPIView(generics.ListAPIView):
    queryset = Company_contact.objects.all()
    serializer_class = Company_contactSerializer

class Feedback_formSerializerAPIView(generics.ListAPIView):
    queryset = Feedback_form.objects.all()
    serializer_class = Feedback_formSerializer