from rest_framework import generics
from django.shortcuts import render
from .models import Project, Image,Slider_image, Company_contact, Application_form
from .serializers import ProjectSerializer, ImageSerializer,Slider_imageSerializer, Company_contactSerializer, Application_formSerializer


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectOneAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ImageAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class Slider_imageAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = Slider_imageSerializer

class Company_contactAPIView(generics.ListAPIView):
    queryset = Company_contact.objects.all()
    serializer_class = Company_contactSerializer

class Application_formSerializerAPIView(generics.ListAPIView):
    queryset = Application_form.objects.all()
    serializer_class = Application_formSerializer