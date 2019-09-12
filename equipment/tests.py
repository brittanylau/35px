from django.test import TestCase, Client

client = Client()
response = client.get('/')


class CameraDetailViewTests(TestCase):
    def test_no_photos(self):
