# Generated by Django 3.1.7 on 2021-05-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_item_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
