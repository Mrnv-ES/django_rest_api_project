from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from todoapp.models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):
    creator = HyperlinkedIdentityField(view_name='creator-detail')

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    project = HyperlinkedIdentityField(view_name='project-detail')
    author = HyperlinkedIdentityField(view_name='author-detail')

    class Meta:
        model = ToDo
        fields = '__all__'
