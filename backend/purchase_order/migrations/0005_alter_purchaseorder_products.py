# Generated by Django 4.2.7 on 2023-11-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0004_purchaseorderproducts_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='po_products', to='purchase_order.purchaseorderproducts'),
        ),
    ]