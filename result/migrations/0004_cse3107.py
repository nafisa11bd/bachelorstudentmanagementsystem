# Generated by Django 2.2.3 on 2019-09-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_cse3105'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSE3107',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField(max_length=10)),
                ('mark', models.IntegerField(max_length=10)),
                ('file', models.FileField(upload_to='abc/')),
            ],
        ),
    ]
