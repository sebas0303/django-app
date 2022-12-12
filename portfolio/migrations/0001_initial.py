# Generated by Django 4.1.4 on 2022-12-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('foto_url', models.URLField()),
                ('github_url', models.URLField()),
            ],
        ),
    ]
