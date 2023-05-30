from rest_framework import serializers
from .models import Project, Image

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name_project', 'type_project')