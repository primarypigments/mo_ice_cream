# Generated by Django 5.0.2 on 2024-02-29 16:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time_slot', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=10)),
                ('location', models.CharField(choices=[('Kakenstorf', 'Kakenstorf'), ('Regesbostel', 'Regesbostel'), ('Brackel', 'Brackel'), ('Regesbostel', 'Brackel'), ('Wistedt', 'Wistedt'), ('Eyendorf', 'Eyendorf')], max_length=25)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Canceled', 'Canceled')], default='Pending', max_length=10)),
                ('book_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
