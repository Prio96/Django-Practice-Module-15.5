# Generated by Django 5.1 on 2024-09-04 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album Name', models.CharField(max_length=200)),
                ('Release_Date', models.DateField(auto_now_add=True)),
                ('Rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('Artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musician.musician')),
            ],
        ),
    ]
