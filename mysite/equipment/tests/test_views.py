from django.test import TestCase, Client
from django.urls import reverse
from equipment.models import Camera, Film, Lens

client = Client()
response = client.get('/')


class CameraDetailViewTests(TestCase):
    def test_no_photos(self):
        for camera in Camera.objects.all():
            response = self.client.get(
                reverse('equipment:camera_detail', kwargs={'pk': camera.id})
            )
            self.assertEqual(response.status_code, 200)
            self.assertQuerysetEqual(response.context['photo_list'], [])

    # TODO: Test for adding posts to a camera and checking that detail page


class FilmDetailViewTests(TestCase):
    def test_no_photos(self):
        for film in Film.objects.all():
            response = self.client.get(
                reverse('equipment:film_detail', kwargs={'pk': film.id})
            )
            self.assertEqual(response.status_code, 200)
            self.assertQuerysetEqual(response.context['photo_list'], [])

    # TODO: Test for adding posts to a film and checking that detail page


class LensDetailViewTests(TestCase):
    def test_no_photos(self):
        for lens in Lens.objects.all():
            response = self.client.get(
                reverse('equipment:lens_detail', kwargs={'pk': lens.id})
            )
            self.assertEqual(response.status_code, 200)
            self.assertQuerysetEqual(response.context['photo_list'], [])

    # TODO: Test for adding posts to a lens and checking that detail page
