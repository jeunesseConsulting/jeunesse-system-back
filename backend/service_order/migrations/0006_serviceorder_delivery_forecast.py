# Generated by Django 4.2.7 on 2023-11-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0005_alter_serviceorder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='delivery_forecast',
            field=models.DateField(blank=True, null=True),
        ),
    ]
