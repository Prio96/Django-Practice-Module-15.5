# Generated by Django 5.1 on 2024-09-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=35)),
                ('Last_Name', models.CharField(max_length=35)),
                ('Email Address', models.EmailField(max_length=254)),
                ('Phone Number', models.CharField(max_length=15)),
                ('Instrument Type', models.CharField(max_length=30)),
            ],
        ),
    ]
