from django.db import models
from django.urls import reverse
from users.models import UserProfile
from equipment.models import Camera, Film, Lens


class Tag(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    class Meta:
        ordering = ['-posted_on']

    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True
    )

    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=200)

    taken_on = models.DateField('date taken')
    posted_on = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name='posts')

    # Equipment
    image = models.ImageField(upload_to='posts')
    camera = models.ForeignKey(
        Camera, related_name='posts',
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    film = models.ForeignKey(
        Film, related_name='posts',
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    lens = models.ForeignKey(
        Lens, related_name='posts',
        on_delete=models.PROTECT,
        null=True, blank=True
    )

    # Capture data
    APERTURES = (
        (1.4, '1.4'),
        (2,   '2'),
        (2.8, '2.8'),
        (4,   '4'),
        (5.6, '5'),
        (8,   '8'),
        (11,  '11'),
        (16,  '16'),
        (22,   '22'),
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
    aperture = models.DecimalField(
        choices=APERTURES,
        max_digits=3, decimal_places=1,
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
        return reverse('photos:post_detail', kwargs={'pk': self.id})


class Comment(models.Model):
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.username + ' said \"' + self.text

    def get_absolute_url(self):
        return reverse('photos:post_detail', kwargs={'pk': self.post.id})
