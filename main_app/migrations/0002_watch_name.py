# Generated by Django 4.1 on 2022-08-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='name',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]