# Generated by Django 2.1.3 on 2018-11-29 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181129_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerprofile',
            name='squad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='squads.Squad'),
        ),
    ]
