# Generated by Django 4.0 on 2024-01-24 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0002_dc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dc',
        ),
        migrations.DeleteModel(
            name='Marvel',
        ),
    ]