# Generated by Django 3.0.7 on 2021-04-27 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carspecs',
            old_name='car_band',
            new_name='car_brand',
        ),
    ]
