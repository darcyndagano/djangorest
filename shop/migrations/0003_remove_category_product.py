# Generated by Django 3.2.5 on 2023-08-23 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
    ]
