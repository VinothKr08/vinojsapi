# Generated by Django 2.2.2 on 2019-06-20 17:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('order_no', models.IntegerField()),
                ('subtitle', models.CharField(max_length=120)),
                ('description', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), size=None)),
                ('example', models.TextField(blank=True)),
                ('output', models.TextField(blank=True)),
            ],
        ),
    ]