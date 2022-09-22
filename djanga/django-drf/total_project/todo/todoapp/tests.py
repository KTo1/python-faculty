import json

from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory, APIClient, APITestCase
from .models import ToDo, Project
from .views import ToDoModelViewSet, ProjectModelViewSet
from usersapp.models import User


class TestToDoModelViewSet(TestCase):
    def setUp(self) -> None:
        self.url = '/api/todos/'
        self.factory = APIRequestFactory()
        self.format = 'json'
        self.admin_pwd = 'kto@kto.rukto@kto.ru'
        self.admin = User.objects.create_superuser('kto', 'kto@kto.ru', self.admin_pwd)
        self.project = Project.objects.create(name='project1', repo='')
        self.data_post= {'project':self.project.id, 'subject':'subject1', 'user': self.admin.id, 'is_active':True}
        self.data = {'project': self.project, 'subject': 'subject1', 'user': self.admin, 'is_active': True}

    #ApiRequestFactory
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ToDoModelViewSet.as_view({'get':'list'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        request = self.factory.post(self.url, self.data_post, format=self.format)
        view = ToDoModelViewSet.as_view({'post':'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        request = self.factory.post(self.url, self.data_post, format=self.format)
        force_authenticate(request, self.admin)

        view = ToDoModelViewSet.as_view({'post':'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # ApiClient
    def test_edit_guest_apiclient(self):
        todo = ToDo.objects.create(**self.data)
        new_subject = 'subject new'
        response = self.client.put(f'{self.url}{todo.id}/', {'subject': new_subject})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin_apiclient(self):
        todo = ToDo.objects.create(**self.data)
        new_subject = 'subject new'
        new_data = json.dumps({'project': self.project.id, 'user': self.admin.id, 'subject': new_subject})

        self.client.login(username=self.admin.username, password=self.admin_pwd)

        response = self.client.put(f'{self.url}{todo.id}/', new_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo.refresh_from_db()

        self.assertEqual(todo.subject, new_subject)

        self.client.logout()

    def tearDown(self) -> None:
        pass


class TestToDoTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = '/api/todos/'
        self.project = Project.objects.create(name='project1', repo='')
        self.admin_pwd = 'kto@kto.rukto@kto.ru'
        self.admin = User.objects.create_superuser('kto', 'kto@kto.ru', self.admin_pwd)
        self.data = {'project': self.project, 'subject': 'subject1', 'user': self.admin, 'is_active': True}

    def test_get_list_testcase(self):
        response= self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin_apiclient(self):
        todo = ToDo.objects.create(**self.data)
        new_subject = 'subject new'
        new_data = json.dumps({'project': self.project.id, 'user': self.admin.id, 'subject': new_subject})

        self.client.login(username=self.admin.username, password=self.admin_pwd)

        response = self.client.put(f'{self.url}{todo.id}/', new_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo.refresh_from_db()

        self.assertEqual(todo.subject, new_subject)

        self.client.logout()

    def tearDown(self) -> None:
        pass


class TestToDoMixer(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/todos/'
        self.project = Project.objects.create(name='project1', repo='')
        self.admin_pwd = 'kto@kto.rukto@kto.ru'
        self.admin = User.objects.create_superuser('kto', 'kto@kto.ru', self.admin_pwd)
        self.data = {'project': self.project, 'subject': 'subject1', 'user': self.admin, 'is_active': True}

    def test_get_list_testcase(self):
        response= self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin_apiclient(self):
        project = mixer.blend(Project)
        todo = mixer.blend(ToDo, project=project)

        new_subject = 'subject new'
        new_data = json.dumps({'project': project.id, 'user': self.admin.id, 'subject': new_subject})

        self.client.login(username=self.admin.username, password=self.admin_pwd)

        response = self.client.put(f'{self.url}{todo.id}/', new_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo.refresh_from_db()

        self.assertEqual(todo.subject, new_subject)

        self.client.logout()

    def tearDown(self) -> None:
        pass


class TestProjectModelViewSet(TestCase):
    def setUp(self) -> None:
        self.url = '/api/projects/'
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.format = 'json'
        self.admin_pwd = 'kto@kto.rukto@kto.ru'
        self.admin = User.objects.create_superuser('kto', 'kto@kto.ru', self.admin_pwd)
        self.data = {'name': 'project1', 'repo': '', 'users': [self.admin.id]}

    #ApiRequestFactory
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectModelViewSet.as_view({'get':'list'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        request = self.factory.post(self.url, self.data, format=self.format)
        view = ProjectModelViewSet.as_view({'post':'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        request = self.factory.post(self.url, self.data, format=self.format)
        force_authenticate(request, self.admin)

        view = ProjectModelViewSet.as_view({'post':'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # ApiClient
    def test_edit_guest_apiclient(self):
        project = Project.objects.create(name='project1', repo='')
        response = self.client.put(f'{self.url}{project.id}/', {'name': 'project2'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin_apiclient(self):

        project = Project.objects.create(name='project1', repo='')
        new_name = 'project2'

        self.client.login(username=self.admin.username, password=self.admin_pwd)

        response = self.client.put(f'{self.url}{project.id}/', {'name': new_name, 'users': [self.admin.id]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project.refresh_from_db()

        self.assertEqual(project.name, new_name)

        self.client.logout()


    def tearDown(self) -> None:
        pass


class TestProjectMixer(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/projects/'
        self.admin_pwd = 'kto@kto.rukto@kto.ru'
        self.admin = User.objects.create_superuser('kto', 'kto@kto.ru', self.admin_pwd)

    def test_get_list_testcase(self):
        response= self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin_apiclient(self):

        project = mixer.blend(Project)
        new_name = 'project2'

        self.client.login(username=self.admin.username, password=self.admin_pwd)

        response = self.client.put(f'{self.url}{project.id}/', {'name': new_name, 'users': [self.admin.id]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project.refresh_from_db()

        self.assertEqual(project.name, new_name)

        self.client.logout()

    def tearDown(self) -> None:
        pass


class TestProjectTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = '/api/projects/'
        self.admin_pwd = 'kto@kto.rukto@kto.ru'
        self.admin = User.objects.create_superuser('kto', 'kto@kto.ru', self.admin_pwd)

    def test_get_list_testcase(self):
        response= self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin_apiclient(self):

        project = Project.objects.create(name='project1', repo='')
        new_name = 'project2'

        self.client.login(username=self.admin.username, password=self.admin_pwd)

        response = self.client.put(f'{self.url}{project.id}/', {'name': new_name, 'users': [self.admin.id]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project.refresh_from_db()

        self.assertEqual(project.name, new_name)

        self.client.logout()

    def tearDown(self) -> None:
        pass