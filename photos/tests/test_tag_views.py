from django.test import TestCase, Client
from django.urls import reverse
from photos.models import Tag

client = Client()
response = client.get('/')


def create_tag(name):
    return Tag.objects.create(name=name)


class TagListViewTests(TestCase):
    def test_no_tags(self):
        response = self.client.get(reverse('photos:tag_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tag_list'], [])

    def test_tag(self):
        create_tag(name="tagname")
        response = self.client.get(reverse('photos:tag_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['tag_list'],
            ['<Tag: tagname>']
        )


class TagDetailViewTests(TestCase):
    def test_no_posts(self):
        for tag in Tag.objects.all():
            response = self.client.get(
                reverse('photos:tag_detail', kwargs={'pk': tag.id})
            )
            self.assertEqual(response.status_code, 200)
            self.assertQuerysetEqual(response.context['photo_list'], [])

    # TODO: Test if there are posts
