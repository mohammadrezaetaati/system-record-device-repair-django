# Generated by Django 4.0.6 on 2022-11-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0007_remove_deviceinput_m_alter_deviceinput_entry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinput',
            name='entry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deviceinput',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deviceinput',
            name='provide_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deviceinput',
            name='repair_city_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deviceinput',
            name='request_date',
            field=models.DateTimeField(),
        ),
    ]
