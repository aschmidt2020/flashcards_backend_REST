# Generated by Django 4.0.1 on 2022-01-26 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Flashcard',
        ),
    ]
