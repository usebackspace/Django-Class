# Generated by Django 5.0.1 on 2024-03-01 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_subtotal_pet_price_and_qunatity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='price_and_Qunatity',
            new_name='price_and_Quantity_total',
        ),
    ]