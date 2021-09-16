from rest_framework.serializers import HyperlinkedModelSerializer
from todoapp.models import Project, ToDo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
