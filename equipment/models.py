from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Camera(models.Model):
    brand = models.ForeignKey(
        Brand, related_name='cameras', on_delete=models.PROTECT, null=True
    )
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.brand.name + ' ' + self.name

 
class Film(models.Model):
    brand = models.ForeignKey(
        Brand, related_name='film', on_delete=models.PROTECT, null=True
    )
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.brand.name + ' ' + self.name


class Lens(models.Model):
    brand = models.ForeignKey(
        Brand, related_name='lenses', on_delete=models.PROTECT, null=True
    )
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.brand.name + ' ' + self.name
