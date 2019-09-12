from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserProfile

client = Client()
response = client.get('/')


def create_user_profile(user):
    return UserProfile.objects.create(user=user)


class UserProfileListViewTests(TestCase):
    def test_no_user_profiles(self):
        response = self.client.get(reverse('users:user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['userprofile_list'], [])

    def test_user_with_profile(self):
        user = User.objects.create_user(username='test', password='password')
        create_user_profile(user)

        response = self.client.get(reverse('users:user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['userprofile_list'],
            ['<UserProfile: test>']
        )

    def test_user_without_profile(self):
        User.objects.create_user(username='test', password='password')

        response = self.client.get(reverse('users:user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['userprofile_list'], [])
