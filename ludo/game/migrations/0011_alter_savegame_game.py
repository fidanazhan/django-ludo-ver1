# Generated by Django 4.1 on 2022-08-14 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_savegame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savegame',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_bookmark', to='game.game'),
        ),
    ]
