from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from todoapp.views import ProjectViewSet
from usersapp.models import User


class TestUserViewSet(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('django', 'superuser@mail.ru', 'geekbrains')

    def test_get_list_no_auth(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Дает доступ неавторизированному пользователю?

    def test_get_list_auth(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_details_no_auth(self):
        user = User.objects.create(username='my_user', email='myuser@mail.ru')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Дает доступ неавторизированному пользователю?

    def test_get_details_auth(self):
        user = User.objects.create(username='my_user', email='myuser@mail.ru')
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_auth(self):
        user = User.objects.create(username='my_user', email='myuser@mail.ru')
        client = APIClient()
        client.login(username='django', password='geekbrains')
        print(client.login(username='django', password='geekbrains'))
        response = client.put(f'/api/users/{user.id}/',
                              {'username': 'my_own_user',
                               'email': 'my_own_user@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.name, 'my_own_user')
        client.logout()
        # Выдает ошибку AssertionError: 403 != 200 (forbidden),
        # при этом client.login = True

