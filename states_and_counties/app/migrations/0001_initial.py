# Generated by Django 5.0.3 on 2024-05-22 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('abbreviation', models.CharField(max_length=2)),
                ('flower', models.CharField(max_length=30)),
                ('capital', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('county_seat', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.state')),
            ],
        ),
    ]
