# Generated by Django 2.2.3 on 2019-10-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0007_auto_20191003_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cse3101',
            name='mark',
            field=models.IntegerField(blank=True, max_length=10),
        ),
    ]
