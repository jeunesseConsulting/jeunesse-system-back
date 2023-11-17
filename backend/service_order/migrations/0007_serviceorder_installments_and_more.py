# Generated by Django 4.2.7 on 2023-11-17 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment_method', '0001_initial'),
        ('service_order', '0006_serviceorder_delivery_forecast'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='installments',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='os_payment_method', to='payment_method.paymentmethod'),
        ),
    ]