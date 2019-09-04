from django.db import models
from django.urls import reverse

# Create your models here.
# class Photographer(models.Model):
#    name = models.CharField(max_length=20)
#    location = models.CharField(max_length=20)

#    def __str__(self):
#        return self.name + ', ' + self.location

class Post(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=200)
    # image = models.FileField()
    # photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    photographer = 'Brittany'
    taken_on = models.DateTimeField('date taken')
    posted_on = models.DateTimeField('date posted')

    def __str__(self):
        return self.title + ', taken by ' + self.photographer

    def get_absolute_url(self):
        return reverse('feed:post_list')
