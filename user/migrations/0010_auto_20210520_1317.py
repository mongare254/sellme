# Generated by Django 3.1.7 on 2021-05-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
