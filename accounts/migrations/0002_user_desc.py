# Generated by Django 3.0.2 on 2020-03-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.CharField(default='default', max_length=1000),
            preserve_default=False,
        ),
    ]