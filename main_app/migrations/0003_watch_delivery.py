# Generated by Django 4.1 on 2022-08-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watch_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='delivery',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
