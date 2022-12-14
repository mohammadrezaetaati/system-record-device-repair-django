# Generated by Django 4.0.6 on 2022-10-30 13:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('boss', models.CharField(max_length=30)),
                ('update', models.CharField(choices=[('update', 'Update'), ('no_update', 'No_update')], default='no_update', max_length=9)),
                ('storekeeper', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('boss', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^[0-9-۰-۹]+$')])),
                ('update', models.CharField(choices=[('update', 'Update'), ('no_update', 'No_update')], default='no_update', max_length=9)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='place.place')),
            ],
            options={
                'ordering': ('place',),
            },
        ),
    ]
