# Generated by Django 2.0.13 on 2019-09-11 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
