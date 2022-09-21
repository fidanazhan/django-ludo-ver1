# Generated by Django 4.1 on 2022-08-14 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_game_request_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]