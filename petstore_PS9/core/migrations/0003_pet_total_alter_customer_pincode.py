# Generated by Django 5.0.1 on 2024-03-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pet_discounted_price_alter_pet_selling_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
