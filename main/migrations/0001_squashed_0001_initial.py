# Generated by Django 3.0.2 on 2020-01-13 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('main', '0001_initial')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('slug', models.SlugField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name_plural': 'faculties',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('file_path', models.FileField(blank=True, upload_to='')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.CharField(choices=[('document', 'Document'), ('powerpoint', 'PowerPoint'), ('video', 'Video')], default='document', max_length=50)),
                ('added_by', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Department')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Level')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Faculty'),
        ),
    ]