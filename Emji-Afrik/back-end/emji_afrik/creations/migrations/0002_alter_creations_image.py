# Generated by Django 5.1.7 on 2025-03-08 10:37

import creations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creations',
            name='image',
            field=models.ImageField(upload_to=creations.models.upload_to_path),
        ),
    ]
