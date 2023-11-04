# Generated by Django 4.2.7 on 2023-11-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('document', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=510)),
                ('zip_code', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
    ]
