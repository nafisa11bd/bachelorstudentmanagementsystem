# Generated by Django 2.2.3 on 2019-10-03 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_cse3109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cse3105',
            name='teacher',
        ),
    ]
