# Generated by Django 4.2.7 on 2023-11-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
    ]
