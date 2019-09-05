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
    image = models.ImageField(upload_to='posts')
    photographer = 'Brittany' # models.ForeignKey(Photographer, on_delete=models.CASCADE)
    taken_on = models.DateField('date taken')
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ', taken by ' + self.photographer

    def get_absolute_url(self):
        return reverse('feed:post_list')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commenter = models.CharField(max_length=50)
    text = models.CharField(max_length = 200)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commenter + ' said \"' + self.text

    def get_absolute_url(self):
        return reverse('feed:post_detail', kwargs={'pk': self.post.id})
