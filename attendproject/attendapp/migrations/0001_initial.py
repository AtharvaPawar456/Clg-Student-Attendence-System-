# Generated by Django 4.2.2 on 2024-04-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentprofile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imgpath', models.CharField(default='attendapp/setup/studentprofileimg/boy avatar.png', max_length=200)),
                ('year', models.IntegerField(default=2024)),
                ('rollno', models.IntegerField(default=0)),
                ('name', models.CharField(default='-', max_length=200)),
                ('div', models.CharField(default='-', max_length=200)),
                ('branch', models.CharField(default='-', max_length=200)),
                ('y1cgpa', models.FloatField(default=0.0, verbose_name='Y1CGPA')),
                ('y1sgpa', models.FloatField(default=0.0, verbose_name='Y1SGPA')),
                ('y2cgpa', models.FloatField(default=0.0, verbose_name='Y2CGPA')),
                ('y2sgpa', models.FloatField(default=0.0, verbose_name='Y2SGPA')),
                ('y3cgpa', models.FloatField(default=0.0, verbose_name='Y3CGPA')),
                ('y3sgpa', models.FloatField(default=0.0, verbose_name='Y3SGPA')),
                ('y4cgpa', models.FloatField(default=0.0, verbose_name='Y4CGPA')),
                ('y4sgpa', models.FloatField(default=0.0, verbose_name='Y4SGPA')),
                ('address', models.CharField(default='-', max_length=1000)),
                ('phoneno', models.CharField(default='-', max_length=200)),
                ('parentphoneno', models.CharField(default='-', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='-', max_length=200)),
                ('phoneno', models.CharField(default='-', max_length=200)),
                ('address', models.CharField(default='-', max_length=1000)),
                ('branch', models.CharField(default='-', max_length=1000)),
                ('div', models.CharField(default='A', max_length=200)),
                ('year', models.IntegerField(default=2024)),
            ],
        ),
    ]
