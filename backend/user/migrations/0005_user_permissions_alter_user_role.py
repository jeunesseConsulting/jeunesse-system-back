# Generated by Django 4.2.7 on 2023-11-06 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_rename_role_role_name'),
        ('permissions', '0002_rename_permission_permissions_name'),
        ('user', '0004_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='user_permissions', to='permissions.permissions'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_role', to='roles.role'),
        ),
    ]
