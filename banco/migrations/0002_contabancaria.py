# Generated by Django 5.1 on 2024-08-24 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_BLR', models.FloatField(blank=True, null=True)),
                ('saldo_USD', models.FloatField(blank=True, null=True)),
                ('saldo_EUR', models.FloatField(blank=True, null=True)),
                ('saldo_BTC', models.FloatField(blank=True, null=True)),
                ('salgo_ARS', models.FloatField(blank=True, null=True)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
