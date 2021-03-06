# Generated by Django 2.1.3 on 2018-11-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181129_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerprofile',
            name='deaths',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='kills',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='rating',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='squad_leader',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='vip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='wallet',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
