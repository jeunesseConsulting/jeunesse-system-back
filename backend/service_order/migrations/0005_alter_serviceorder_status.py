# Generated by Django 4.2.7 on 2023-11-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0004_serviceorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='status',
            field=models.CharField(default='pendente', max_length=255),
        ),
    ]
