# Generated by Django 2.2.2 on 2019-06-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eksapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='picture',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='eksapp/profile_pics'),
        ),
    ]
