from django.urls import path, include
from rest_framework.routers import DefaultRouter
import todoapp.views as todoapp

todoapp_router = DefaultRouter()
todoapp_router.register('projects', todoapp.ProjectViewSet, basename='project')
todoapp_router.register('todos', todoapp.ToDoViewSet, basename='todo')

urlpatterns = [
    path('view/set/', include(todoapp_router.urls)),
]
