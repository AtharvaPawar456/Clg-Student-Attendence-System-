# Generated by Django 4.2.2 on 2024-04-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendapp', '0002_remove_teacherdata_branch_remove_teacherdata_div_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherdata',
            name='emailid',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
