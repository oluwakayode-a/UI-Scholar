# Generated by Django 3.0.2 on 2020-02-06 00:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_material_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='material',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Material'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
