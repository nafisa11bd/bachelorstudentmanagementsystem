# Generated by Django 2.2.3 on 2019-09-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSE3101',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField(max_length=10)),
                ('mark', models.IntegerField(max_length=10)),
            ],
        ),
    ]
