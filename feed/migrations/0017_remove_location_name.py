# Generated by Django 2.0.13 on 2019-09-06 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0016_auto_20190906_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
    ]