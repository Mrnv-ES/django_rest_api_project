from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from todoapp.filters import ToDoFilter
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, ToDoModelSerializer


class SmallPagination(PageNumberPagination):
    page_size = 10


class BigPagination(PageNumberPagination):
    page_size = 20


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        qs = Project.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__contains=name)
        return qs


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = BigPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ToDoFilter

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
