# Generated by Django 4.2.7 on 2023-11-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_permissions_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=40),
        ),
    ]
