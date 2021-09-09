from django_filters import rest_framework as filters
from todoapp.models import ToDo


class ToDoFilter(filters.FilterSet):
    project = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ToDo
        fields = ['project']
