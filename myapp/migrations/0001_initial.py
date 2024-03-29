# Generated by Django 5.0.1 on 2024-01-24 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GameSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('gamemode', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battleTag', models.CharField(max_length=255)),
                ('toonname', models.CharField(max_length=255)),
                ('last_avatarId', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('mmr', models.IntegerField()),
                ('searchRace', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('avatarId', models.CharField(max_length=50)),
                ('division', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('game_setting', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.gamesetting')),
                ('player', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.player')),
            ],
        ),
    ]
