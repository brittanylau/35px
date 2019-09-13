# Generated by Django 2.0.13 on 2019-09-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20190913_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='aperture',
            field=models.PositiveIntegerField(blank=True, choices=[(14, '1.4'), (20, '2'), (28, '2.8'), (40, '4'), (56, '5.6'), (80, '8'), (110, '11'), (160, '16'), (220, '22')], null=True),
        ),
    ]
