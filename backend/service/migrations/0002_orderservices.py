# Generated by Django 4.2.7 on 2023-11-09 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.BigIntegerField()),
                ('price', models.FloatField(default=0.0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_aux', to='service.service')),
            ],
            options={
                'db_table': 'aux_order_services',
            },
        ),
    ]
