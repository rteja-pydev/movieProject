# Generated by Django 2.2 on 2021-02-27 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesinfo', '0002_auto_20210227_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='rdate',
            new_name='ryear',
        ),
    ]
