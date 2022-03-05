# Generated by Django 3.2.8 on 2022-01-22 03:48

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Kusa', '0003_delete_friendslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='null', max_length=30)),
                ('FriendList', djongo.models.fields.JSONField(default=[])),
                ('SteamID', models.CharField(default='null', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(default='000000', max_length=30)),
                ('Name', models.CharField(default='null', max_length=30)),
                ('Email', models.CharField(default='123@123', max_length=30)),
                ('SteamID', models.CharField(default='7890', max_length=30)),
                ('Achievements', models.CharField(default='null', max_length=120)),
                ('Blocked', models.CharField(default='null', max_length=120)),
                ('Friends', models.CharField(default='null', max_length=120)),
                ('FriendsRequest', models.CharField(default='null', max_length=120)),
                ('ProfilePic', models.CharField(default='whatever', max_length=120)),
            ],
        ),
    ]