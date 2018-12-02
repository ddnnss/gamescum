# Generated by Django 2.1.3 on 2018-12-02 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('users', '0005_auto_20181129_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerprofile',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='rating',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=4),
        ),
    ]