# Generated by Django 4.0.6 on 2022-11-26 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0013_alter_deviceinput_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinput',
            name='work_order_number',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex='^[0-9۰-۹]{4}\\/[0-9۰−۹]*$')]),
        ),
    ]
