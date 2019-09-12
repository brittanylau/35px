import json
import tempfile

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from PIL import Image

from photos.models import Photo
from users.models import UserProfile


class ImageUploadAPITestCase(APITestCase):
    url = reverse('photos:image-upload-api')

    def setUp(self):
        self.username = 'hello'
        self.password = 'world'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.profile = UserProfile.objects.create(user=self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_upload_auth(self):
        """
        Authenticated users can upload a new image, which will create a new post
        with the current user as its author.
        """

        self.client.login(username=self.username, password=self.password)

        image = Image.new('RGB', (100, 100))
        temp = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp)
        temp.seek(0)

        response = self.client.post(
            self.url,
            {'image': temp},
            format='multipart'
        )

        self.assertEqual(201, response.status_code)

        author = Photo.objects.get(id=1).author
        self.assertEqual(author, self.profile)

    def test_upload_no_auth(self):
        """
        Unauthenticated users cannot upload new images.
        """

        image = Image.new('RGB', (100, 100))
        temp = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp)
        temp.seek(0)

        response = self.client.post(
            self.url,
            {'image': temp},
            format='multipart'
        )

        self.assertEqual(403, response.status_code)


class PhotoAPITestCase(APITestCase):
    url = reverse('photos:photo-list')

    def setUp(self):
        self.username = 'hello'
        self.password = 'world'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.profile = UserProfile.objects.create(user=self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # TODO: def test_create_post_auth(self):
    # TODO: def test_update_post_auth(self):
    # TODO: def test_delete_post_auth(self):
    # TODO: def test_create_post_no_auth(self):
    # TODO: def test_update_post_no_auth(self):
    # TODO: def test_delete_post_no_auth(self):
