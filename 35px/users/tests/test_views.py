from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserProfile

client = Client()
response = client.get('/')


def create_user_profile(username):
    user = User.objects.create_user(username, password='password')
    return UserProfile.objects.create(user=user)


class UserProfileListViewTests(TestCase):
    def test_no_profiles(self):
        response = self.client.get(reverse('users:user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['userprofile_list'], [])

    def test_one_profile(self):
        profile = create_user_profile('testuser')

        response = self.client.get(reverse('users:user_list'))
        self.assertContains(
            response,
            profile.user.username,
            count=1,
            status_code=200
        )
        self.assertQuerysetEqual(
            response.context['userprofile_list'],
            ['<UserProfile: testuser>']
        )


class UserProfileDetailViewTests(TestCase):
    def test_no_photos(self):
        create_user_profile('testuser1')
        create_user_profile('testuser2')
        create_user_profile('testuser3')

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
        profile = create_user_profile('testuser')
        # TODO: create photos

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
