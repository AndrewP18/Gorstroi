from rest_framework import serializers
from .models import Project, Image,Slider_image, Company_contact, Application_form


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class Slider_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider_image
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class Company_contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_contact
        fields = "__all__"


class Application_formSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application_form
        fields = "__all__"