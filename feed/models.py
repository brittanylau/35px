from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts')
    taken_on = models.DateField('date taken')
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ', taken by ' + self.user.name

    def get_absolute_url(self):
        return reverse('feed:post_list')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    text = models.CharField(max_length = 200)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + ' said \"' + self.text

    def get_absolute_url(self):
        return reverse('feed:post_detail', kwargs={'pk': self.post.id})
