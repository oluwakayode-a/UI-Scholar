# Generated by Django 3.0.2 on 2020-02-08 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200208_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='user',
        ),
    ]