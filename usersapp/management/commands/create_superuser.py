from django.core.management import BaseCommand
from usersapp.models import User


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     parser.add_argument('superuser', type=str)

    def handle(self, *args, **options):
        # User.objects.all().delete()
        # superuser = options['superuser']
        user = User.objects.create_superuser(username=f'django',
                                             first_name=f'first_name_superuser',
                                             last_name=f'last_name_superuser',
                                             email=f'superuser@mail.ru',
                                             password='geekbrains')
        print(f'{user} has been created')
