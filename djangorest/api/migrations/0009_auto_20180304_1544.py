# Generated by Django 2.0.2 on 2018-03-04 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180304_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameslist',
            old_name='fondmemories',
            new_name='fond_memories',
        ),
    ]
