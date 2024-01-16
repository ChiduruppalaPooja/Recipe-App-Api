# Generated by Django 3.2.23 on 2024-01-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('category_name_id', models.IntegerField(unique=True)),
                ('category_image_url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
    ]