# Generated by Django 4.0.6 on 2022-11-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_alter_deviceinput_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deviceinput',
            options={'ordering': ('-entry_date',)},
        ),
        migrations.AddField(
            model_name='deviceinput',
            name='m',
            field=models.DateField(blank=True, null=True),
        ),
    ]
