# Generated by Django 2.0.13 on 2019-09-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
