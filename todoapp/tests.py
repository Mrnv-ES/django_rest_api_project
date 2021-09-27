from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from todoapp.models import Project
from todoapp.views import ProjectViewSet
from mixer.backend.django import mixer
import json


class TestUserViewSet(APITestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_user('django', 'superuser@mail.ru', 'geekbrains')

    def test_get_list(self):
        self.client.force_login(user=self.superuser)
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_mixer(self):
    #     project = mixer.blend(Project)
    #     # print(project.name, project.repository)
    #     self.client.force_login(user=self.superuser)
    #     response = self.client.put(f'/api/projects/{project.id}/',
    #                                {'name': 'my_project',
    #                                 'repository': project.repository})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        project = mixer.blend(Project, name='my_own_project')
        print(project.name, project.repository)
        self.client.force_login(user=self.superuser)
        response = self.client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_project = json.loads(response.content)
        self.assertEqual(response_project['name'], 'my_own_project')
