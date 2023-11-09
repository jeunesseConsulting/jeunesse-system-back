# Generated by Django 4.2.7 on 2023-11-09 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_client_birth_date_client_gender'),
        ('vehicle', '0003_alter_vehicle_owner'),
        ('service', '0002_orderservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='os_client', to='client.client')),
                ('services', models.ManyToManyField(blank=True, related_name='os_services', to='service.orderservices')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='os_vehicle', to='vehicle.vehicle')),
            ],
            options={
                'db_table': 'service_order',
            },
        ),
    ]
