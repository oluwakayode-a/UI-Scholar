# Generated by Django 3.0.2 on 2020-02-08 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_material_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='university',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.University'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.University'),
            preserve_default=False,
        ),
    ]