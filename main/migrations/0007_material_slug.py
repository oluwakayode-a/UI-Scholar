# Generated by Django 3.0.2 on 2020-02-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200208_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
