# Generated by Django 4.2.4 on 2023-11-01 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='person_name',
        ),
    ]