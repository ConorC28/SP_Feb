# Generated by Django 2.0.2 on 2018-02-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_gameslist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameslist',
            name='game_pic',
            field=models.ImageField(default='../static/None/no-img.jpg', upload_to='../static/'),
        ),
    ]
