# Generated by Django 4.2.7 on 2023-11-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0006_alter_purchaseorderproducts_purchase_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderproducts',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
