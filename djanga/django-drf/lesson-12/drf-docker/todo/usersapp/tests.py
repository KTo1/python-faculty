from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from .models import User
from .views import UserModelViewSet


class TestUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = '/api/users/'

    def test_get_list_testcase(self):
        response= self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass


class TestUserModelViewSet(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.url = '/api/users/'
        self.format = 'json'
        self.data = {'username':'kto1', 'email':'kto1@kto.ru', 'password':'kto1@kto.ru'}
        self.admin = User.objects.create_superuser('kto', 'kto@kto.ru', 'kto@kto.rukto@kto.ru')

    #ApiRequestFactory
    def test_get_list(self):
        request =self.factory.get(self.url)
        view = UserModelViewSet.as_view({'get':'list'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Создавать пользователей запрещено
    def test_create_guest(self):
        pass
        # request = self.factory.post(self.url, self.data, format=self.format)
        # view = UserModelViewSet.as_view({'post':'create'})
        # response = view(request)
        #
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #ApiClient
    def test_get_detail_apiclient(self):
        response = self.client.get(f'{self.url}{self.admin.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass

