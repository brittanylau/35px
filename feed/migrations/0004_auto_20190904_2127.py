# Generated by Django 2.0.13 on 2019-09-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20190904_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='taken_on',
            field=models.DateField(verbose_name='date taken'),
        ),
    ]
