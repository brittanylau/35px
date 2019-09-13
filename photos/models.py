from django.db import models
from django.urls import reverse
from users.models import UserProfile
from equipment.models import Camera, Film, Lens


class Tag(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):

    class Meta:
        ordering = ['-posted_on']

    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='photos',
        null=True
    )

    image = models.ImageField(upload_to='photos', blank=False, null=False)

    title = models.CharField(max_length=50, blank=True)
    caption = models.CharField(max_length=200, blank=True)
    posted_on = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(
        Tag, related_name='photos', blank=True
    )

    # Equipment

    camera = models.ForeignKey(
        Camera, related_name='photos',
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    film = models.ForeignKey(
        Film, related_name='photos',
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    lens = models.ForeignKey(
        Lens, related_name='photos',
        on_delete=models.PROTECT,
        null=True, blank=True
    )

    # Capture data

    APERTURES = (
        (14,  '1.4'),
        (20,  '2'),
        (28,  '2.8'),
        (40,  '4'),
        (56,  '5.6'),
        (80,  '8'),
        (110, '11'),
        (160, '16'),
        (220, '22'),
    )
    SHUTTER_SPEEDS = (
        (1,    '1'),
        (2,    '1/2'),
        (4,    '1/4'),
        (8,    '1/8'),
        (15,   '1/15'),
        (30,   '1/30'),
        (60,   '1/60'),
        (125,  '1/125'),
        (250,  '1/250'),
        (500,  '1/500'),
        (1000, '1/1000'),
        (2000, '1/2000'),
        (4000, '1/4000'),
    )
    EXPOSURES = (
        (100, '100'),
        (200, '200'),
        (400, '400'),
        (800, '800'),
        (1600, '1600'),
    )
    aperture = models.PositiveIntegerField(
        choices=APERTURES,
        null=True, blank=True
    )
    shutter_speed = models.PositiveIntegerField(
        choices=SHUTTER_SPEEDS,
        null=True, blank=True
    )
    exposure = models.PositiveIntegerField(
        choices=EXPOSURES,
        null=True, blank=True
    )

    def __str__(self):
        return self.title + ', taken by ' + self.author.user.username

    def get_absolute_url(self):
        return reverse('photos:photo_detail', kwargs={'pk': self.id})


class Comment(models.Model):
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.username + ' said \"' + self.text

    def get_absolute_url(self):
        return reverse('photos:photo_detail', kwargs={'pk': self.photo.id})
