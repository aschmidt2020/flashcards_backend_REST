# Generated by Django 4.0.1 on 2022-01-26 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcard', '0003_flashcard_user_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcard.collection'),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
