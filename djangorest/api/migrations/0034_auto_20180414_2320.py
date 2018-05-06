# Generated by Django 2.0.2 on 2018-04-14 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0033_auto_20180406_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articleslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('article', models.CharField(max_length=225)),
                ('user_rating', multiselectfield.db.fields.MultiSelectField(choices=[('0.5', '0.5'), ('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0'), ('5.5', '5.5'), ('6.0', '6.0'), ('6.5', '6.5'), ('7.0', '7.0'), ('7.5', '7.5'), ('8.0', '8.0'), ('8.5', '8.5'), ('9.0', '9.0'), ('9.5', '9.5'), ('10', '10')], max_length=78)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=5000)),
                ('fond_memories', models.CharField(max_length=10000)),
                ('game_pic', models.ImageField(default='game_image', upload_to='game_image')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articleslist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='gameslist',
            name='game_pic',
            field=models.ImageField(default='game_image', upload_to='game_image'),
        ),
    ]
