# Generated by Django 4.0.4 on 2022-05-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oppo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=250)),
                ('short_url', models.CharField(max_length=50, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
