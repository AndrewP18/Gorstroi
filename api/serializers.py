from rest_framework import serializers
from .models import Project, Image, Company_contact, Feedback_form


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
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

class Feedback_formSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback_form
        fields = "__all__"