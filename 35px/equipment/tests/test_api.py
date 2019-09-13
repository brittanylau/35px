import json

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class CameraAPITestCase(APITestCase):
    url = reverse('equipment:camera-list')

    def setUp(self):
        self.username = 'hello'
        self.password = 'world'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_delete_camera_auth(self):

        self.client.login(username=self.username, password=self.password)

        brand_name = 'Minolta'
        camera_name = 'X-700'
        response = self.client.post(
            self.url,
            {"brand": {"name": brand_name}, "name": camera_name},
            format='json'
        )
        self.assertEqual(201, response.status_code)

        response = self.client.get(self.url)
        camera = json.loads(response.content)[0]

        self.assertEqual(camera['brand']['name'], brand_name)
        self.assertEqual(camera['name'], camera_name)

    def test_create_camera_no_auth(self):
        brand_name = 'Minolta'
        camera_name = 'X-700'
        response = self.client.post(
            self.url,
            {"brand": {"name": brand_name}, "name": camera_name},
            format='json'
        )
        self.assertEqual(403, response.status_code)

    # TODO: def test_delete_camera_no_auth(self):


class FilmAPITestCase(APITestCase):
    url = reverse('equipment:film-list')

    def setUp(self):
        self.username = 'hello'
        self.password = 'world'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_film_auth(self):

        self.client.login(username=self.username, password=self.password)

        brand_name = 'Kodak'
        film_name = 'Portra'
        response = self.client.post(
            self.url,
            {"brand": {"name": brand_name}, "name": film_name},
            format='json'
        )
        self.assertEqual(201, response.status_code)

        response = self.client.get(self.url)
        film = json.loads(response.content)[0]

        self.assertEqual(film['brand']['name'], brand_name)
        self.assertEqual(film['name'], film_name)

    def test_create_film_no_auth(self):
        brand_name = 'Kodak'
        film_name = 'Portra'
        response = self.client.post(
            self.url,
            {"brand": {"name": brand_name}, "name": film_name},
            format='json'
        )
        self.assertEqual(403, response.status_code)


class LensAPITestCase(APITestCase):
    url = reverse('equipment:lens-list')

    def setUp(self):
        self.username = 'hello'
        self.password = 'world'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_camera_auth(self):

        self.client.login(username=self.username, password=self.password)

        brand_name = 'Nikon'
        lens_name = 'Nikkor'
        response = self.client.post(
            self.url,
            {"brand": {"name": brand_name}, "name": lens_name},
            format='json'
        )
        self.assertEqual(201, response.status_code)

        response = self.client.get(self.url)
        film = json.loads(response.content)[0]

        self.assertEqual(film['brand']['name'], brand_name)
        self.assertEqual(film['name'], lens_name)

    def test_create_camera_no_auth(self):
        brand_name = 'Nikon'
        lens_name = 'Nikkor'
        response = self.client.post(
            self.url,
            {"brand": {"name": brand_name}, "name": lens_name},
            format='json'
        )
        self.assertEqual(403, response.status_code)
