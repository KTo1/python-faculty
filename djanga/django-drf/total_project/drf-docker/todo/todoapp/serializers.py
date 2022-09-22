from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'repo', 'users']


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'project', 'subject', 'user', 'created', 'updated', 'is_active']