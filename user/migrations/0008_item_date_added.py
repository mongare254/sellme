# Generated by Django 3.1.7 on 2021-05-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210517_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
