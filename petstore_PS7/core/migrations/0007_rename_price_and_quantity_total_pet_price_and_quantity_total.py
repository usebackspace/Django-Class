# Generated by Django 5.0.1 on 2024-03-01 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_price_and_qunatity_pet_price_and_quantity_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='price_and_Quantity_total',
            new_name='price_and_quantity_total',
        ),
    ]