from rest_framework import serializers
from multiverse.models import Metaverse
#from projects.api.serializers import ProjectSerializer
from projects.models import Project


class ProjectMetaverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']


class MultiverseSerializer(serializers.Serializer):
    name = serializers.CharField()


class MetaverseSerializer(serializers.ModelSerializer):
    project_info = ProjectMetaverseSerializer(source='project')
    class Meta:
        model = Metaverse
        fields = '__all__'
        #fields = ['id', 'project_info',]

