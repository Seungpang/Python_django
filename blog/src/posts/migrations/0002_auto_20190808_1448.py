# Generated by Django 2.2.4 on 2019-08-08 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumnail',
            new_name='thumbnail',
        ),
    ]
