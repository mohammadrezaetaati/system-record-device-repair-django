# Generated by Django 4.0.6 on 2022-11-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0008_alter_deviceinput_entry_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='part',
            options={'ordering': ('category__name', 'name', 'brand')},
        ),
    ]