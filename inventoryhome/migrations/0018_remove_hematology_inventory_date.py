# Generated by Django 3.0.4 on 2020-04-24 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryhome', '0017_hematology_inventory_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hematology_inventory',
            name='date',
        ),
    ]
