# Generated by Django 5.0.2 on 2024-04-04 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_properties_city_properties_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='description',
        ),
    ]