# Generated by Django 4.1 on 2022-08-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_watch_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='delivery',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
