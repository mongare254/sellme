# Generated by Django 3.1.7 on 2021-05-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20210524_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(default='registration', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interested',
            name='amount_paid',
            field=models.IntegerField(blank=True, default='500'),
        ),
    ]