# Generated by Django 4.2.2 on 2024-04-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendapp', '0003_teacherdata_emailid'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='teachername',
            field=models.CharField(default='Sahil', max_length=200),
        ),
    ]
