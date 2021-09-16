import random
from django.core.management.base import BaseCommand
from todoapp.models import Project, ToDo
from usersapp.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('project_num', type=int)
        parser.add_argument('todo_num', type=int)

    def handle(self, *args, **options):
        users = User.objects.all()
        Project.objects.all().delete()
        project_num = options['project_num']
        project_lst = []
        for i in range(project_num):
            project = Project.objects.create(name=f'project_{i}',
                                             repository=f'http://127.0.0.1:8000/projects/project_{i}/')
            for j in range(random.randrange(5)):
                project.users.add(random.choice(users))
            project.save()
            project_lst.append(project)
        print(f'{project_num} projects have been created')

        ToDo.objects.all().delete()
        todo_num = options['todo_num']
        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
            for i in range(todo_num):
                project = random.choice(project_lst)
                ToDo.objects.create(project=project,
                                    note_text=f'text_{i}' * 9,
                                    author=random.choice(users))
            print(f'{todo_num} todo-notes have been created')
        else:
            print('no superuser found')
