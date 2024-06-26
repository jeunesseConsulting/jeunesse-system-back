# Generated by Django 4.2.7 on 2023-11-08 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=7)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('fabrication_year', models.CharField(max_length=4)),
                ('vehicle_type', models.CharField(db_column='type', max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vehicles',
            },
        ),
    ]
