# Generated by Django 4.2.2 on 2023-06-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='site',
            field=models.CharField(choices=[('https://mahsulot.com/order_api/', 'mahsulot.com'), ('https://airshop.uz/order_api/', 'airshop.uz')], max_length=255),
        ),
    ]
