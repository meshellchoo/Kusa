# Generated by Django 3.2.8 on 2022-02-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kusa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='steamuser',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='steamuser',
            name='emailsEnabled',
            field=models.BooleanField(default=True),
        ),
    ]