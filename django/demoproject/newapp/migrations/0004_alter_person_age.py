# Generated by Django 4.2.4 on 2023-11-01 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
