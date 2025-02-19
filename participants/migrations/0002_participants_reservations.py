# Generated by Django 4.2 on 2024-10-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0002_alter_conference_category'),
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='reservations',
            field=models.ManyToManyField(related_name='Reservation', through='participants.Reservation', to='conference.conference'),
        ),
    ]
