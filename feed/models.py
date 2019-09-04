from django.db import models

# Create your models here.
class Photographer(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ', ' + self.location

class Photo(models.Model):
    # photo
    title = models.CharField(max_length=50)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title + ', taken by ' + self.photographer.name
