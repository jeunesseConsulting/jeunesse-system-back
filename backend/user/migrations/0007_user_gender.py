# Generated by Django 4.2.7 on 2023-11-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_document_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]