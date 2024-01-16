# Generated by Django 3.2.23 on 2024-01-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('food_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_type_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'food_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100, unique=True)),
                ('item_description', models.CharField(blank=True, max_length=100, null=True)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('cgst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sgst', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'items',
                'managed': False,
            },
        ),
    ]