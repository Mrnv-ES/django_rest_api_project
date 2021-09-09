from django.core.management import BaseCommand
from usersapp.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('users_number', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        users_number = options['users_number']
        for i in range(users_number):
            user = User.objects.create_user(username=f'username{i}',
                                            first_name=f'first_name{i}',
                                            last_name=f'last_name{i}',
                                            email=f'email{i}@mail.ru')
            print(f'{user} has been created')
        print('finished')
