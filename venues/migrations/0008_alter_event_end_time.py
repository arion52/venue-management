# Generated by Django 5.1.2 on 2024-10-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0007_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
