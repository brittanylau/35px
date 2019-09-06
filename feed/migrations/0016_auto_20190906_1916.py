# Generated by Django 2.0.13 on 2019-09-06 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_remove_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='aperture',
            field=models.DecimalField(blank=True, choices=[(1.4, '1.4'), (2, '2'), (2.8, '2.8'), (4, '4'), (5.6, '5'), (8, '8'), (11, '11'), (16, '16'), (22, '22')], decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='camera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='feed.Camera'),
        ),
        migrations.AlterField(
            model_name='post',
            name='exposure',
            field=models.PositiveIntegerField(blank=True, choices=[(100, '100'), (200, '200'), (400, '400'), (800, '800'), (1600, '1600')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='feed.Film'),
        ),
        migrations.AlterField(
            model_name='post',
            name='lens',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='feed.Lens'),
        ),
        migrations.AlterField(
            model_name='post',
            name='shutter_speed',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '1/2'), (4, '1/4'), (8, '1/8'), (15, '1/15'), (30, '1/30'), (60, '1/60'), (125, '1/125'), (250, '1/250'), (500, '1/500'), (1000, '1/1000'), (2000, '1/2000'), (4000, '1/4000')], null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
