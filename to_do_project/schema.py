import graphene
from graphene_django import DjangoObjectType

from todoapp.models import Project, ToDo
from usersapp.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(ToDoType)
    todos_by_project = graphene.List(ToDoType, project=graphene.Int(required=True))
    users_by_superusers = graphene.List(UserType, is_superuser=graphene.Boolean(required=True))
    projects_by_name = graphene.List(ProjectType, name=graphene.String(required=True))

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    def resolve_todos_by_project(self, info, project):
        return ToDo.objects.filter(project=project)

    def resolve_users_by_superusers(self, info, is_superuser):
        return User.objects.filter(is_superuser=is_superuser)

    def resolve_projects_by_name(self, info, name):
        return Project.objects(name=name)

schema = graphene.Schema(query=Query)
