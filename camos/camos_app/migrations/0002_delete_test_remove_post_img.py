# Generated by Django 4.1.4 on 2022-12-14 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camos_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]