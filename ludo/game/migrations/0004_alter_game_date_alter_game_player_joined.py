# Generated by Django 4.1 on 2022-08-09 05:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0003_remove_game_date_updated_remove_game_game_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_joined',
            field=models.ManyToManyField(blank=True, null=True, related_name='joined_player', to=settings.AUTH_USER_MODEL),
        ),
    ]