# Generated by Django 5.1.5 on 2025-01-21 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiawTeachers',
            fields=[
                ('nom', models.CharField(default='M Raoul', max_length=255, primary_key=True, serialize=False, verbose_name="nom de l'enseignant")),
                ('telephone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('jour', models.DateField(default=datetime.date.today, help_text='Format de la date : AAAA-MM-JJ', primary_key=True, serialize=False, verbose_name='jour de la semaine')),
                ('cours', models.CharField(default='', help_text='Intitule du cours dans', max_length=255, verbose_name='intitule cu cours')),
                ('enseignant', models.CharField(help_text="Nom de l'enseignant", max_length=255, verbose_name="Nom de l'enseignant")),
                ('teacherTel', models.IntegerField(help_text="Entre le numero de l'enseignant")),
            ],
        ),
    ]
