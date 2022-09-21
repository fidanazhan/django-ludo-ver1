# Generated by Django 4.1 on 2022-08-14 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0011_alter_savegame_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark_game', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='SaveGame',
        ),
        migrations.AddField(
            model_name='bookmarkgame',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_bookmark', to='game.game'),
        ),
    ]
