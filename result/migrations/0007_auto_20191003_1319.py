# Generated by Django 2.2.3 on 2019-10-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0006_remove_cse3105_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cse3101',
            name='id',
        ),
        migrations.AlterField(
            model_name='cse3101',
            name='roll',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
