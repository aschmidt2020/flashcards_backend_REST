# Generated by Django 4.0.1 on 2022-01-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=250)),
                ('collection', models.CharField(max_length=250)),
            ],
        ),
    ]