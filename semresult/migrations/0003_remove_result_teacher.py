# Generated by Django 2.2.3 on 2019-09-28 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semresult', '0002_auto_20190927_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='teacher',
        ),
    ]
