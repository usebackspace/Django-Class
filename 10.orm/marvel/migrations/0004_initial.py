# Generated by Django 5.0.1 on 2024-01-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marvel', '0003_delete_dc_delete_marvel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marvel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('heroic_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
