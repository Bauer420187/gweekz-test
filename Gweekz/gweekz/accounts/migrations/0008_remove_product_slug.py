# Generated by Django 3.2.4 on 2021-08-14 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
