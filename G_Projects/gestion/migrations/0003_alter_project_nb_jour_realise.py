# Generated by Django 4.0.5 on 2022-07-04 08:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_alter_project_en_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='nb_jour_realise',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
