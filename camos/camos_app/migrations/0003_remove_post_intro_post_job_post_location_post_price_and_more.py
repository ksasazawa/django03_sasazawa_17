# Generated by Django 4.1.4 on 2022-12-14 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('camos_app', '0002_delete_test_remove_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='intro',
        ),
        migrations.AddField(
            model_name='post',
            name='job',
            field=models.CharField(default="test", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default="test", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='qualification',
            field=models.CharField(default="test", max_length=255),
            preserve_default=False,
        ),
    ]
