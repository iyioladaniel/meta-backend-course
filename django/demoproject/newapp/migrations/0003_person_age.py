# Generated by Django 4.2.4 on 2023-11-01 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_rename_name_person_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
