# Generated by Django 5.1.1 on 2024-10-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_booked', models.BooleanField(default=False)),
                ('booked_by', models.CharField(blank=True, max_length=100, null=True)),
                ('booked_at', models.DateTimeField(blank=True, null=True)),
                ('booking_duration', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
