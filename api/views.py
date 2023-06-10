from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Project, Image, Slider_image, Company_contact, Application_form
from .serializers import ProjectSerializer, ImageSerializer,Slider_imageSerializer, Company_contactSerializer, Application_formSerializer


class Projects_list(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes =(IsAuthenticatedOrReadOnly, )

class ProjectOne(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes =(IsAuthenticatedOrReadOnly, )

class Images_list(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes =(IsAuthenticatedOrReadOnly, )

class Slider_images_list(generics.ListAPIView):
    queryset = Slider_image.objects.all()
    serializer_class = Slider_imageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class Company_contacts_list(generics.ListAPIView):
    queryset = Company_contact.objects.all()
    serializer_class = Company_contactSerializer
    permission_classes =(IsAuthenticatedOrReadOnly, )

class Application_form_create(generics.CreateAPIView):
    queryset = Application_form.objects.all()
    serializer_class = Application_formSerializer
    permission_classes =(IsAuthenticatedOrReadOnly, )