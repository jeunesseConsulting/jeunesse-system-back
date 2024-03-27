# Generated by Django 4.2.7 on 2024-03-20 02:06

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
            name='FinancialEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_type', models.CharField(max_length=1)),
                ('entry_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('origin', models.IntegerField(blank=True, null=True)),
                ('value', models.FloatField()),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='financial_entry_responsible', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]