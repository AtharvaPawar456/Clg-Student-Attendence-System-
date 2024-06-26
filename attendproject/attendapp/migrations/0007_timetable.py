# Generated by Django 4.2.2 on 2024-04-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendapp', '0006_delete_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('branch', models.CharField(default='-', max_length=200)),
                ('year', models.CharField(default='-', max_length=200)),
                ('div', models.CharField(default='-', max_length=200)),
                ('day', models.CharField(default='-', max_length=200)),
                ('starttime', models.CharField(default='-', max_length=200)),
                ('endtime', models.CharField(default='-', max_length=200)),
                ('leacture', models.CharField(default='-', max_length=200)),
                ('lectProf', models.CharField(default='-', max_length=200)),
                ('status', models.CharField(default='present', max_length=200)),
            ],
        ),
    ]
