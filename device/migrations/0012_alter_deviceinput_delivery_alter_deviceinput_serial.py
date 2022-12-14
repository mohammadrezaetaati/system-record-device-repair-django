# Generated by Django 4.0.6 on 2022-11-21 07:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0011_alter_deviceinput_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinput',
            name='delivery',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex='^[ا-ی\\s]*$')]),
        ),
        migrations.AlterField(
            model_name='deviceinput',
            name='serial',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[0-9۰-۹]{2,10}$')]),
        ),
    ]
