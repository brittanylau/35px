from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserProfile

client = Client()
response = client.get('/')


class UserProfileListViewTests(TestCase):
    def test_no_profiles(self):
        response = self.client.get(reverse('users:user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['userprofile_list'], [])

    def test_one_profile(self):
        username = 'testuser'
        User.objects.create_user(username)

        response = self.client.get(reverse('users:user_list'))
        self.assertContains(
            response,
            username,
            count=1,
            status_code=200
        )
        self.assertQuerysetEqual(
            response.context['userprofile_list'],
            ['<UserProfile: testuser>']
        )


class UserProfileDetailViewTests(TestCase):
    def test_no_photos(self):
        User.objects.create_user(username='testuser1')
        User.objects.create_user(username='testuser2')
        User.objects.create_user(username='testuser3')

        for profile in UserProfile.objects.all():
            response = self.client.get(
                reverse('users:user_detail', kwargs={'pk': profile.id})
            )
            self.assertContains(
                response,
                profile.user.username,
                count=1,
                status_code=200
            )
            # self.assertQuerysetEqual(response.context[''], [])

    def test_photos(self):
        username = 'testuser'
        user = User.objects.create_user(username)
        # TODO: create photos

        response = self.client.get(
            reverse('users:user_detail', kwargs={'pk': user.profile.id})
        )
        self.assertContains(
            response,
            username,
            count=1,
            status_code=200
        )
        # self.assertQuerysetEqual(response.context[''], [])
