# Generated by Django 3.2.13 on 2023-01-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.URLField()),
                ('new', models.URLField(default='')),
                ('expire', models.DateTimeField()),
            ],
        ),
    ]
