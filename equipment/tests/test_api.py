import json

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class CameraAPITestCase(APITestCase):
    url = reverse('equipment:camera-list')

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_camera(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            self.url,
            {
                "brand": {
                    "name": "Minolta"
                },
                "name": "X-700"
            },
            format='json'
        )
        self.assertEqual(201, response.status_code)

        response = self.client.get(self.url)
        camera = json.loads(response.content)[0]

        self.assertEqual(
            camera['brand']['name'],
            "Minolta"
        )
        self.assertEqual(
            camera['name'],
            "X-700"
        )


class FilmAPITestCase(APITestCase):
    url = reverse('equipment:film-list')

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_film(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            self.url,
            {
                "brand": {
                    "name": "Kodak"
                },
                "name": "Portra"
            },
            format='json'
        )
        self.assertEqual(201, response.status_code)

        response = self.client.get(self.url)
        film = json.loads(response.content)[0]

        self.assertEqual(
            film['brand']['name'],
            "Kodak"
        )
        self.assertEqual(
            film['name'],
            "Portra"
        )


class LensAPITestCase(APITestCase):
    url = reverse('equipment:lens-list')

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_camera(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            self.url,
            {
                "brand": {
                    "name": "Nikon"
                },
                "name": "Nikkor"
            },
            format='json'
        )
        self.assertEqual(201, response.status_code)

        response = self.client.get(self.url)
        film = json.loads(response.content)[0]

        self.assertEqual(
            film['brand']['name'],
            "Nikon"
        )
        self.assertEqual(
            film['name'],
            "Nikkor"
        )
