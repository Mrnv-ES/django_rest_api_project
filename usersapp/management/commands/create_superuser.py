from django.core.management import BaseCommand
from usersapp.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('superuser', type=str)

    def handle(self, *args, **options):
        User.objects.all().delete()
        superuser = options['superuser']
        user = User.objects.create_superuser(username=f'username_{superuser}',
                                             first_name=f'first_name_{superuser}',
                                             last_name=f'last_name_{superuser}',
                                             email=f'email_{superuser}@mail.ru',
                                             password='geekbrains')
        print(f'{user} has been created')
