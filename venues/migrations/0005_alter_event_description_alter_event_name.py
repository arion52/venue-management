# Generated by Django 5.1.1 on 2024-10-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0004_venue_booked_at_venue_booked_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]